"""Data model package for md-terminology-trove."""

from pathlib import Path
from .md_terminology_trove import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "md_terminology_trove.yaml"
