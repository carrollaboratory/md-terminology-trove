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
                 'term_cross_reference',
                 'concept_relationship'],
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



class Vocabulary(ConfiguredBaseModel):
    """
    Flat table containing each of the ontologies used for dataset annotations
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/ontology',
         'slot_usage': {'vocabulary_id': {'identifier': True,
                                          'name': 'vocabulary_id',
                                          'range': 'string'}}})

    vocabulary_id: str = Field(default=..., title="Vocabulary ID", description="""The ID associated with the vocabulary or ontology inside the warehouse""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary', 'Concept']} })
    name: Optional[str] = Field(default=None, title="Vocabulary Name", description="""Full name for the ontology""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary']} })
    vocabulary_uri: str = Field(default=..., title="Vocabulary URI", description="""Official URI associated with the vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary']} })
    fhir_system: str = Field(default=..., title="FHIR System", description="""System used within FHIR valuesets and codings""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary']} })
    prefix: Optional[str] = Field(default=None, title="Canonical Curie Prefix", description="""The authoritative namespace prefix allocated to the vocabulary. Used to resolve compact identifiers (CURIEs) to their full semantic URIs or FHIR system URLs.""", json_schema_extra = { "linkml_meta": {'comments': ['Must start with a letter; thereafter allows letters, digits, '
                      'underscores, hyphens, and dots to accommodate OLS/UMLS source '
                      'variability.',
                      'RISK: In order for all of our data to correctly join, the '
                      'format of the prefix must always align with the prefix used in '
                      'this table.'],
         'domain_of': ['Vocabulary'],
         'todos': ['Ensure that MapDragon and TermWeaver both rely on the same rules '
                   'for prefixes']} })
    description: Optional[str] = Field(default=None, title="Ontology description", description="""Ontology description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary']} })
    version: Optional[str] = Field(default=None, title="Version", description="""Version associated with the current vocabulary content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary']} })
    source: Optional[str] = Field(default=None, title="Data source", description="""Source used for populating the terminologies members""", json_schema_extra = { "linkml_meta": {'comments': ["This is currently poorly defined because we haven't fully "
                      'defined the nature of the data pulls. Most likely it will end '
                      'up as a filename (.owl, .obo, etc) or another tool, etc'],
         'domain_of': ['Vocabulary']} })

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


class Concept(ConfiguredBaseModel):
    """
    Flat table containing the curied codes for all ontological terms used for dataset annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/term-concept',
         'slot_usage': {'concept_curie': {'identifier': True,
                                          'name': 'concept_curie',
                                          'range': 'uriorcurie',
                                          'required': True}}})

    concept_curie: str = Field(default=..., title="Concept Curie", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'HierarchyMap',
                       'CrossReference',
                       'ConceptRelationship']} })
    vocabulary_id: str = Field(default=..., title="Vocabulary ID", description="""The ID associated with the vocabulary or ontology inside the warehouse""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vocabulary', 'Concept']} })
    concept_code: str = Field(default=..., title="Concept Code", description="""Identifier as it is defined within the ontology""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    omop_concept_id: Optional[int] = Field(default=None, title="OMOP Concept ID", description="""The OMOP Concept ID for the term, if applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    display: Optional[str] = Field(default=None, title="Display", description="""The friendly display string of the coded term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    definition: Optional[str] = Field(default=None, title="Definition", description="""Detailed description for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    dbt_updated_at: datetime  = Field(default=..., description="""The timestamp when the source record was last changed, used by dbt to detect if an update has occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    dbt_valid_from: datetime  = Field(default=..., description="""The timestamp indicating when this specific row's historical version became active.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    dbt_valid_to: Optional[datetime ] = Field(default=None, description="""The timestamp indicating when this historical version was superseded. It remains NULL if the row is the currently active version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    dbt_scd_id: Optional[str] = Field(default=None, description="""Reserved for dbt SCD Type 2 tracking. Kept NULL until dbt migration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })


class HierarchyMap(ConfiguredBaseModel):
    """
    Basic parent/child relationships, suitable for populating a hierarchical FHIR codesystem
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/term-hierarchy-map'})

    concept_curie: Optional[str] = Field(default=None, title="Concept Curie", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'HierarchyMap',
                       'CrossReference',
                       'ConceptRelationship']} })
    parent_concept_curie: Optional[str] = Field(default=None, title="Parent Concept Curie", description="""The immediate ancester of the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['HierarchyMap']} })


class CrossReference(ConfiguredBaseModel):
    """
    References to other terms that are encountered during traversal/loading
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/term-cross-reference'})

    concept_curie: Optional[str] = Field(default=None, title="Concept Curie", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'HierarchyMap',
                       'CrossReference',
                       'ConceptRelationship']} })
    target_concept_curie: Optional[str] = Field(default=None, title="Target Concept ID", description="""The concept to which this term relates""", json_schema_extra = { "linkml_meta": {'domain_of': ['CrossReference', 'ConceptRelationship']} })
    mapping_relationship: Optional[EnumMappingRelationship] = Field(default=None, title="Mapping Relationship", description="""The relationship between the subject (this term) and the object (target_concept_id)""", json_schema_extra = { "linkml_meta": {'domain_of': ['CrossReference']} })


class ConceptRelationship(ConfiguredBaseModel):
    """
    Relationships between two terms.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/carrollaboratory/md-terminology-trove/concept-relationship'})

    concept_curie: Optional[str] = Field(default=None, title="Concept Curie", description="""The standardized curie for the term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'HierarchyMap',
                       'CrossReference',
                       'ConceptRelationship']} })
    target_concept_curie: Optional[str] = Field(default=None, title="Target Concept ID", description="""The concept to which this term relates""", json_schema_extra = { "linkml_meta": {'domain_of': ['CrossReference', 'ConceptRelationship']} })
    relationship_curie: Optional[str] = Field(default=None, title="Mapping Relationship", description="""The relationship between the subject (this term) and the object (target_concept_id)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConceptRelationship']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Vocabulary.model_rebuild()
Concept.model_rebuild()
HierarchyMap.model_rebuild()
CrossReference.model_rebuild()
ConceptRelationship.model_rebuild()
