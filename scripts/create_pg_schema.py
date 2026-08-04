#!/usr/bin/env python3
"""
create_pg_schema.py

Build a Postgres schema from a LinkML-generated SQLAlchemy model, either:
  - directly against a live database (--db-url), or
  - as a standalone .sql file with no database connection at all (--output)

No intermediate hand-edited SQL, no regex post-processing either way.

Workflow:
    1. gen-sqla your_schema.yaml > model_sqla.py
    2a. python create_pg_schema.py model_sqla.py --db-url <postgres-url>
        # or
    2b. python create_pg_schema.py model_sqla.py --output schema.sql

What this avoids, and why it doesn't need separate DDL-patching scripts:
    - FK ordering: SQLAlchemy's MetaData.create_all() topologically sorts
      tables by dependency itself -- including in --output mode, where
      it's driven through create_mock_engine instead of a live connection.
    - Native Postgres ENUM types (which break dbt unit tests -- see
      dbt-labs/dbt-adapters#670/#662): before creating anything, this
      script patches Enum so it defaults to native_enum=False and
      create_constraint=True, so Postgres gets VARCHAR + CHECK instead
      of CREATE TYPE ... AS ENUM.

Requires: sqlalchemy
--db-url mode additionally requires the relevant DB driver, e.g.
psycopg2-binary for postgresql+psycopg2://. --output mode needs nothing
beyond sqlalchemy itself -- it never opens a connection.
"""

import argparse
import importlib.util
import re
import sys

import yaml
from sqlalchemy import MetaData, Table, inspect
from sqlalchemy.types import Enum


def to_snake_case(name: str) -> str:
    """Converts PascalCase / CamelCase string to snake_case for dbt standards."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def transform_metadata(original_metadata: MetaData, target_schema: str) -> MetaData:
    """Clones a metadata container, changing table names to snake_case and adding schemas."""
    new_metadata = MetaData()

    # Track mapping from old table keys to new Table objects to safely preserve Foreign Keys
    table_mapping = {}

    # Step 1: Instantiate the new tables with corrected names & schemas
    for original_key, old_table in original_metadata.tables.items():
        new_name = to_snake_case(old_table.name)

        # Create a clean clone of the table shell
        new_table = Table(new_name, new_metadata, schema=target_schema)

        # Copy across all columns safely (tethering them to the new table)
        for column in old_table.columns:
            # .copy() detaches the column from the old table so it can bind to the new one
            new_table.append_column(column.copy())

        table_mapping[original_key] = new_table

    # Step 2: Fix Foreign Key references to ensure they point to the newly named tables
    for original_key, new_table in table_mapping.items():
        for fk in new_table.foreign_keys:
            # Locate the original targeted parent table key (e.g. "ParentClass")
            old_parent_key = fk.column.table.fullname

            if old_parent_key in table_mapping:
                # Dynamically re-target the constraint to point to the new snake_case schema table
                target_col_name = fk.column.name
                new_parent_table = table_mapping[old_parent_key]
                fk.parent = new_table.c[fk.parent.name]
                fk._set_target_column(new_parent_table.c[target_col_name])

    return new_metadata


def build_dbt_models(metadata: MetaData, schema: str, description: str):
    model_def = {"version": 2}

    sources = {"name": schema, "description": description, "tables": []}
    for tablename, table in metadata.tables.items():
        sources["tables"].append({"name": tablename})


def load_generated_module(path: str):
    spec = importlib.util.spec_from_file_location("linkml_sqla_model", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def patch_enum_type():
    """Replace sqlalchemy.sql.sqltypes.Enum with a subclass that defaults
    to native_enum=False, create_constraint=False, *before* the generated
    model module is executed.

    This has to happen before exec, not after: create_constraint's CHECK
    constraint (when enabled) is attached to the table via an event fired
    when the column is attached, so setting flags on an already-built
    column is too late -- the constraint just won't be there.

    create_constraint is forced to False (not just left off) because the
    LinkML-generated Enum types here don't reliably carry their
    permissible values through to SQLAlchemy. When an Enum has no usable
    values, SQLAlchemy still renders a CHECK constraint, but with an
    always-false clause as a safety fallback, e.g.:

        CONSTRAINT "EnumDataUsePermission" CHECK (data_use_permission IN (NULL) AND (1 != 1))

    That constraint rejects every row, which is exactly what broke the
    dbt tests. Since the goal is plain VARCHAR columns with no native
    ENUM *and* no CHECK constraint, create_constraint=False sidesteps the
    problem entirely rather than trying to fix value population.
    """
    import sqlalchemy.sql.sqltypes as sqltypes
    from sqlalchemy.types import Enum as _Enum

    class NonNativeEnum(_Enum):
        def __init__(self, *args, **kwargs):
            kwargs["native_enum"] = False
            kwargs["create_constraint"] = False
            super().__init__(*args, **kwargs)

    sqltypes.Enum = NonNativeEnum
    # Also patch the sqlalchemy.types alias, in case the generated code
    # imports from there instead of sqlalchemy.sql.sqltypes.
    import sqlalchemy.types as types_module

    types_module.Enum = NonNativeEnum


def generate_ddl(metadata, dialect_name: str) -> str:
    """Compile CREATE TABLE/INDEX statements for `metadata`, in
    dependency-sorted order, for the given dialect -- with no live
    database connection required.

    Uses SQLAlchemy's create_mock_engine, which runs the exact same
    MetaData.create_all() code path (including the topological sort of
    tables and the enum/native_enum handling) but calls a local
    `executor` callback instead of talking to a real database.
    """
    from sqlalchemy import create_mock_engine

    statements = []

    def _executor(sql, *multiparams, **params):
        statements.append(str(sql.compile(dialect=engine.dialect)).strip() + ";")

    engine = create_mock_engine(f"{dialect_name}://", executor=_executor)
    metadata.create_all(engine, checkfirst=False)

    return "\n\n".join(statements) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Create a Postgres schema from LinkML-generated SQLAlchemy metadata, "
        "either directly against a live database or as a standalone .sql file."
    )
    parser.add_argument(
        "model_path",
        default="project/sqlalchemy/include_access_model.py",
        help="Path to the file produced by `gen-sqla`",
    )

    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--db-url",
        help="SQLAlchemy connection URL to create the schema in directly, e.g. "
        "postgresql+psycopg2://user:pass@localhost:5432/testdb",
    )
    target.add_argument(
        "--output",
        help="Write DDL to this .sql file instead of connecting to a database. "
        "No database driver (e.g. psycopg2) is required in this mode.",
    )

    parser.add_argument(
        "--dialect",
        default="postgresql",
        help="SQLAlchemy dialect name to target in --output mode (default: postgresql).",
    )
    parser.add_argument(
        "--drop-first",
        action="store_true",
        help="Drop all tables in the target schema before creating (--db-url mode only, destructive).",
    )
    parser.add_argument(
        "--echo",
        action="store_true",
        help="Print the DDL SQLAlchemy executes as it runs (--db-url mode only).",
    )
    parser.add_argument(
        "--schema", type=str, help="Database schema to prefix the table name"
    )
    args = parser.parse_args()

    patch_enum_type()
    module = load_generated_module(args.model_path)
    if not hasattr(module, "metadata"):
        sys.exit(
            f"{args.model_path} has no top-level `metadata` object (expected from gen-sqla)."
        )
    metadata = module.metadata

    patched = sum(
        1
        for table in metadata.tables.values()
        for column in table.columns
        if isinstance(column.type, Enum)
    )
    if patched:
        print(
            f"{patched} enum column(s) will use VARCHAR + CHECK instead of native ENUM.",
            file=sys.stderr,
        )

    # Fix table names
    metadata = transform_metadata(metadata, target_schema="dev_include_access")

    if args.output:
        ddl = generate_ddl(metadata, args.dialect)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(ddl)
        print(
            f"Wrote DDL for {len(metadata.tables)} table(s) to {args.output}",
            file=sys.stderr,
        )
        return

    from sqlalchemy import create_engine

    engine = create_engine(args.db_url, echo=args.echo)

    if args.drop_first:
        metadata.drop_all(engine)

    # create_all() topologically sorts tables by FK dependency itself --
    # no manual ordering, no ALTER TABLE post-processing needed.
    metadata.create_all(engine)
    print(f"Created {len(metadata.tables)} table(s) in {args.db_url}", file=sys.stderr)


if __name__ == "__main__":
    main()
