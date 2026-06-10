from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'md_terminology_trove',
     'default_range': 'string',
     'description': 'Data model that represents the flattened ontologies that are '
                    'used by MapDragon for annotation.',
     'id': 'https://w3id.org/carrollaboratory/md-terminology-trove',
     'imports': ['linkml:types',
                 'term_ontology',
                 'term_concept',
                 'term_hierarchy_map',
                 'term_cross_reference'],
     'license': 'MIT',
     'name': 'md-terminology-trove',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'http://www.example.org/rdf#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'md_terminology_trove': {'prefix_prefix': 'md_terminology_trove',
                                           'prefix_reference': 'https://w3id.org/carrollaboratory/md-terminology-trove/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'}},
     'see_also': ['https://carrollaboratory.github.io/md-terminology-trove'],
     'source_file': 'src/md_terminology_trove/schema/md_terminology_trove.yaml',
     'title': 'md-terminology-trove'} )

class EnumMappingRelationship(str, Enum):
    """
    SKOS terms for mapping relationships
    """
    exact_match = "exact_match"
    """
    The two codes can be used interchangeably across almost all systems
    """
    close_match = "close_match"
    """
    The two are similar enough to be interchangeable in some contexts, but not all.
    """
    broad_match = "broad_match"
    """
    The object (target) is a broader/more general concept than the subject (concept_id).
    """
    narrow_match = "narrow_match"
    """
    The object (target) is a narrower/more specific concept than the subject (concept_id).
    """
    related_match = "related_match"
    """
    The two are associated in some way, but not interchangeable.
    """



class TermOntology(ConfiguredBaseModel):
    """
    Flat table containing each of the ontologies used for dataset annotations
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/ontology',
         'slot_usage': {'ontology_id': {'identifier': True,
                                        'name': 'ontology_id',
                                        'range': 'string'}}})

    ontology_id: str = Field(default=..., title="Ontology ID", description="""The ID associated with the ontology inside the warehouse""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermOntology', 'TermConcept']} })
    name: Optional[str] = Field(default=None, title="Ontology Name", description="""Full name for the ontology""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermOntology']} })
    ontology_uri: str = Field(default=..., title="Ontology URI", description="""Official URI associated with the ontology""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermOntology']} })
    fhir_system: str = Field(default=..., title="FHIR System", description="""System used within FHIR valuesets and codings""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermOntology']} })
    prefix: Optional[str] = Field(default=None, title="Canonical Curie Prefix", description="""The authoritative namespace prefix allocated to the vocabulary. Used to resolve compact identifiers (CURIEs) to their full semantic URIs or FHIR system URLs.""", json_schema_extra = { "linkml_meta": {'comments': ['Must start with a letter; thereafter allows letters, digits, '
                      'underscores, hyphens, and dots to accommodate OLS/UMLS source '
                      'variability.',
                      'RISK: In order for all of our data to correctly join, the '
                      'format of the prefix must always align with the prefix used in '
                      'this table.'],
         'domain_of': ['TermOntology'],
         'todos': ['Ensure that MapDragon and TermWeaver both rely on the same rules '
                   'for prefixes']} })
    description: Optional[str] = Field(default=None, title="Ontology description", description="""Ontology description""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermOntology']} })
    source: Optional[str] = Field(default=None, title="Data source", description="""Source used for populating the terminologies members""", json_schema_extra = { "linkml_meta": {'comments': ["This is currently poorly defined because we haven't fully "
                      'defined the nature of the data pulls. Most likely it will end '
                      'up as a filename (.owl, .obo, etc) or another tool, etc'],
         'domain_of': ['TermOntology']} })

    @field_validator('prefix')
    def pattern_prefix(cls, v):
        pattern=re.compile(r"^[A-Za-z][A-Za-z0-9_\-\.]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid prefix format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid prefix format: {v}"
            raise ValueError(err_msg)
        return v


class HasConceptId(ConfiguredBaseModel):
    """
    Base class for all concept tables
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove'})

    concept_id: str = Field(default=..., title="Concept ID", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasConceptId']} })


class TermConcept(HasConceptId):
    """
    Flat table containing the curied codes for all ontological terms used for dataset annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/term-concept',
         'slot_usage': {'concept_id': {'identifier': True,
                                       'name': 'concept_id',
                                       'range': 'uriorcurie'}}})

    ontology_id: str = Field(default=..., title="Ontology ID", description="""The ID associated with the ontology inside the warehouse""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermOntology', 'TermConcept']} })
    concept_code: str = Field(default=..., title="Concept Code", description="""Identifier as it is defined within the ontology""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    display: Optional[str] = Field(default=None, title="Display", description="""The friendly display string of the coded term""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    definition: Optional[str] = Field(default=None, title="Definition", description="""Detailed description for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    version: Optional[str] = Field(default=None, title="Version", description="""Version associated with the current ontology content""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    dbt_updated_at: datetime  = Field(default=..., description="""The timestamp when the source record was last changed, used by dbt to detect if an update has occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    dbt_valid_from: datetime  = Field(default=..., description="""The timestamp indicating when this specific row's historical version became active.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    dbt_valid_to: Optional[datetime ] = Field(default=None, description="""The timestamp indicating when this historical version was superseded. It remains NULL if the row is the currently active version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    dbt_scd_id: Optional[str] = Field(default=None, description="""Reserved for dbt SCD Type 2 tracking. Kept NULL until dbt migration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermConcept']} })
    concept_id: str = Field(default=..., title="Concept ID", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasConceptId']} })


class TermHierarchyMap(HasConceptId):
    """
    Basic parent/child relationships, suitable for populating a hierarchical FHIR codesystem    is_a: HasConceptId
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/term-hierarchy-map',
         'slot_usage': {'concept_id': {'name': 'concept_id', 'range': 'TermConcept'}}})

    parent_id: Optional[list[str]] = Field(default=None, title="Parent ID", description="""The immediate ancester of the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermHierarchyMap']} })
    concept_id: str = Field(default=..., title="Concept ID", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasConceptId']} })


class TermCrossReference(HasConceptId):
    """
    References to other terms that are encountered during traversal/loading
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/term-cross-reference',
         'slot_usage': {'concept_id': {'name': 'concept_id', 'range': 'TermConcept'}}})

    target_concept_id: Optional[str] = Field(default=None, title="Target Concept ID", description="""The concept to which this term relates""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermCrossReference']} })
    mapping_relationship: Optional[EnumMappingRelationship] = Field(default=None, title="Mapping Relationship", description="""The relationship between the subject (this term) and the object (target_concept_id)""", json_schema_extra = { "linkml_meta": {'domain_of': ['TermCrossReference']} })
    concept_id: str = Field(default=..., title="Concept ID", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasConceptId']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
TermOntology.model_rebuild()
HasConceptId.model_rebuild()
TermConcept.model_rebuild()
TermHierarchyMap.model_rebuild()
TermCrossReference.model_rebuild()
