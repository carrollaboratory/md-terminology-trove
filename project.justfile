## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540
[group('model development')]
_gen_sqla:
    mkdir -p {{dest}}/sqlalchemy && \
    uv run gen-sqla {{source_schema_path}} --declarative > {{dest}}/sqlalchemy/{{schema_name}}.py

_gen_dbt_model: _gen_sqla
    mkdir -p {{dest}}/dbt && \
    uv run python scripts/gen-dbt-model.py --output {{dest}}/dbt/{{schema_name}}.yml

_gen_dbt_sql: _gen_dbt_model
    mkdir -p {{dest}}/dbt &&\
    uv run python scripts/create_pg_schema.py {{dest}}/sqlalchemy/{{schema_name}}.py --output {{dest}}/dbt/{{schema_name}}.sql



_dbt: _gen_dbt_sql
