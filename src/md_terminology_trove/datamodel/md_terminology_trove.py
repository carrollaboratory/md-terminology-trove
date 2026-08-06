# Auto generated from md_terminology_trove.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-06T16:03:55
# Schema: md-terminology-trove
#
# id: https://w3id.org/carrollaboratory/md-terminology-trove
# description: Data model that represents the flattened ontologies that are used by MapDragon for annotation.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.11.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MD_TERMINOLOGY_TROVE = CurieNamespace('md_terminology_trove', 'https://w3id.org/carrollaboratory/md-terminology-trove/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = MD_TERMINOLOGY_TROVE


# Types

# Class references
class VocabularyVocabularyId(extended_str):
    pass


class ConceptConceptCurie(URIorCURIE):
    pass


@dataclass(repr=False)
class Vocabulary(YAMLRoot):
    """
    Flat table containing each of the ontologies used for dataset annotations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["ontology/Vocabulary"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:ontology/Vocabulary"
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.Vocabulary

    vocabulary_id: Union[str, VocabularyVocabularyId] = None
    vocabulary_uri: Union[str, URI] = None
    fhir_system: Union[str, URI] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vocabulary_id):
            self.MissingRequiredField("vocabulary_id")
        if not isinstance(self.vocabulary_id, VocabularyVocabularyId):
            self.vocabulary_id = VocabularyVocabularyId(self.vocabulary_id)

        if self._is_empty(self.vocabulary_uri):
            self.MissingRequiredField("vocabulary_uri")
        if not isinstance(self.vocabulary_uri, URI):
            self.vocabulary_uri = URI(self.vocabulary_uri)

        if self._is_empty(self.fhir_system):
            self.MissingRequiredField("fhir_system")
        if not isinstance(self.fhir_system, URI):
            self.fhir_system = URI(self.fhir_system)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.prefix is not None and not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    Flat table containing the curied codes for all ontological terms used for dataset annotations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["term-concept/Concept"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:term-concept/Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.Concept

    concept_curie: Union[str, ConceptConceptCurie] = None
    vocabulary_id: Union[str, VocabularyVocabularyId] = None
    concept_code: str = None
    dbt_updated_at: Union[str, XSDDateTime] = None
    dbt_valid_from: Union[str, XSDDateTime] = None
    omop_concept_id: Optional[int] = None
    display: Optional[str] = None
    definition: Optional[str] = None
    dbt_valid_to: Optional[Union[str, XSDDateTime]] = None
    dbt_scd_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_curie):
            self.MissingRequiredField("concept_curie")
        if not isinstance(self.concept_curie, ConceptConceptCurie):
            self.concept_curie = ConceptConceptCurie(self.concept_curie)

        if self._is_empty(self.vocabulary_id):
            self.MissingRequiredField("vocabulary_id")
        if not isinstance(self.vocabulary_id, VocabularyVocabularyId):
            self.vocabulary_id = VocabularyVocabularyId(self.vocabulary_id)

        if self._is_empty(self.concept_code):
            self.MissingRequiredField("concept_code")
        if not isinstance(self.concept_code, str):
            self.concept_code = str(self.concept_code)

        if self._is_empty(self.dbt_updated_at):
            self.MissingRequiredField("dbt_updated_at")
        if not isinstance(self.dbt_updated_at, XSDDateTime):
            self.dbt_updated_at = XSDDateTime(self.dbt_updated_at)

        if self._is_empty(self.dbt_valid_from):
            self.MissingRequiredField("dbt_valid_from")
        if not isinstance(self.dbt_valid_from, XSDDateTime):
            self.dbt_valid_from = XSDDateTime(self.dbt_valid_from)

        if self.omop_concept_id is not None and not isinstance(self.omop_concept_id, int):
            self.omop_concept_id = int(self.omop_concept_id)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.dbt_valid_to is not None and not isinstance(self.dbt_valid_to, XSDDateTime):
            self.dbt_valid_to = XSDDateTime(self.dbt_valid_to)

        if self.dbt_scd_id is not None and not isinstance(self.dbt_scd_id, str):
            self.dbt_scd_id = str(self.dbt_scd_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HierarchyMap(YAMLRoot):
    """
    Basic parent/child relationships, suitable for populating a hierarchical FHIR codesystem
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["term-hierarchy-map/HierarchyMap"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:term-hierarchy-map/HierarchyMap"
    class_name: ClassVar[str] = "HierarchyMap"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.HierarchyMap

    concept_curie: Optional[Union[str, ConceptConceptCurie]] = None
    parent_concept_curie: Optional[Union[str, ConceptConceptCurie]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.concept_curie is not None and not isinstance(self.concept_curie, ConceptConceptCurie):
            self.concept_curie = ConceptConceptCurie(self.concept_curie)

        if self.parent_concept_curie is not None and not isinstance(self.parent_concept_curie, ConceptConceptCurie):
            self.parent_concept_curie = ConceptConceptCurie(self.parent_concept_curie)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrossReference(YAMLRoot):
    """
    References to other terms that are encountered during traversal/loading
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["term-cross-reference/CrossReference"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:term-cross-reference/CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.CrossReference

    concept_curie: Optional[Union[str, ConceptConceptCurie]] = None
    target_concept_curie: Optional[Union[str, ConceptConceptCurie]] = None
    mapping_relationship: Optional[Union[str, "EnumMappingRelationship"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.concept_curie is not None and not isinstance(self.concept_curie, ConceptConceptCurie):
            self.concept_curie = ConceptConceptCurie(self.concept_curie)

        if self.target_concept_curie is not None and not isinstance(self.target_concept_curie, ConceptConceptCurie):
            self.target_concept_curie = ConceptConceptCurie(self.target_concept_curie)

        if self.mapping_relationship is not None and not isinstance(self.mapping_relationship, EnumMappingRelationship):
            self.mapping_relationship = EnumMappingRelationship(self.mapping_relationship)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptRelationship(YAMLRoot):
    """
    Relationships between two terms.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["concept-relationship/ConceptRelationship"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:concept-relationship/ConceptRelationship"
    class_name: ClassVar[str] = "ConceptRelationship"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.ConceptRelationship

    concept_curie: Optional[Union[str, ConceptConceptCurie]] = None
    target_concept_curie: Optional[Union[str, ConceptConceptCurie]] = None
    relationship_curie: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.concept_curie is not None and not isinstance(self.concept_curie, ConceptConceptCurie):
            self.concept_curie = ConceptConceptCurie(self.concept_curie)

        if self.target_concept_curie is not None and not isinstance(self.target_concept_curie, ConceptConceptCurie):
            self.target_concept_curie = ConceptConceptCurie(self.target_concept_curie)

        if self.relationship_curie is not None and not isinstance(self.relationship_curie, URIorCURIE):
            self.relationship_curie = URIorCURIE(self.relationship_curie)

        super().__post_init__(**kwargs)


# Enumerations
class EnumMappingRelationship(EnumDefinitionImpl):
    """
    SKOS terms for mapping relationships
    """
    exact_match = PermissibleValue(
        text="exact_match",
        description="The two codes can be used interchangeably across almost all systems",
        meaning=SKOS["exactMatch"])
    close_match = PermissibleValue(
        text="close_match",
        description="The two are similar enough to be interchangeable in some contexts, but not all.",
        meaning=SKOS["closeMatch"])
    broad_match = PermissibleValue(
        text="broad_match",
        description="The object (target) is a broader/more general concept than the subject (concept_id).",
        meaning=SKOS["broadMatch"])
    narrow_match = PermissibleValue(
        text="narrow_match",
        description="The object (target) is a narrower/more specific concept than the subject (concept_id).",
        meaning=SKOS["narrowMatch"])
    related_match = PermissibleValue(
        text="related_match",
        description="The two are associated in some way, but not interchangeable.",
        meaning=SKOS["relatedMatch"])

    _defn = EnumDefinition(
        name="EnumMappingRelationship",
        description="SKOS terms for mapping relationships",
    )

# Slots
class slots:
    pass

slots.vocabulary_id = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/vocabulary_id'], name="vocabulary_id", curie=MD_TERMINOLOGY_TROVE.curie('ontology/vocabulary_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.vocabulary_id, domain=None, range=Union[str, VocabularyVocabularyId])

slots.name = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/name'], name="name", curie=MD_TERMINOLOGY_TROVE.curie('ontology/name'),
                   model_uri=MD_TERMINOLOGY_TROVE.name, domain=None, range=Optional[str])

slots.vocabulary_uri = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/vocabulary_uri'], name="vocabulary_uri", curie=MD_TERMINOLOGY_TROVE.curie('ontology/vocabulary_uri'),
                   model_uri=MD_TERMINOLOGY_TROVE.vocabulary_uri, domain=None, range=Union[str, URI])

slots.fhir_system = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/fhir_system'], name="fhir_system", curie=MD_TERMINOLOGY_TROVE.curie('ontology/fhir_system'),
                   model_uri=MD_TERMINOLOGY_TROVE.fhir_system, domain=None, range=Union[str, URI])

slots.prefix = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/prefix'], name="prefix", curie=MD_TERMINOLOGY_TROVE.curie('ontology/prefix'),
                   model_uri=MD_TERMINOLOGY_TROVE.prefix, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z][A-Za-z0-9_\-\.]*$'))

slots.description = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/description'], name="description", curie=MD_TERMINOLOGY_TROVE.curie('ontology/description'),
                   model_uri=MD_TERMINOLOGY_TROVE.description, domain=None, range=Optional[str])

slots.version = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/version'], name="version", curie=MD_TERMINOLOGY_TROVE.curie('ontology/version'),
                   model_uri=MD_TERMINOLOGY_TROVE.version, domain=None, range=Optional[str])

slots.source = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/source'], name="source", curie=MD_TERMINOLOGY_TROVE.curie('ontology/source'),
                   model_uri=MD_TERMINOLOGY_TROVE.source, domain=None, range=Optional[str])

slots.concept_curie = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_curie'], name="concept_curie", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_curie'),
                   model_uri=MD_TERMINOLOGY_TROVE.concept_curie, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.concept_code = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_code'], name="concept_code", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_code'),
                   model_uri=MD_TERMINOLOGY_TROVE.concept_code, domain=None, range=str)

slots.omop_concept_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/omop_concept_id'], name="omop_concept_id", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/omop_concept_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.omop_concept_id, domain=None, range=Optional[int])

slots.deprecated = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/deprecated'], name="deprecated", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/deprecated'),
                   model_uri=MD_TERMINOLOGY_TROVE.deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.replaced_by = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/replaced_by'], name="replaced_by", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/replaced_by'),
                   model_uri=MD_TERMINOLOGY_TROVE.replaced_by, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.dbt_scd_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/dbt_scd_id'], name="dbt_scd_id", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/dbt_scd_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.dbt_scd_id, domain=None, range=Optional[str])

slots.dbt_updated_at = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/dbt_updated_at'], name="dbt_updated_at", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/dbt_updated_at'),
                   model_uri=MD_TERMINOLOGY_TROVE.dbt_updated_at, domain=None, range=Union[str, XSDDateTime])

slots.dbt_valid_from = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/dbt_valid_from'], name="dbt_valid_from", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/dbt_valid_from'),
                   model_uri=MD_TERMINOLOGY_TROVE.dbt_valid_from, domain=None, range=Union[str, XSDDateTime])

slots.dbt_valid_to = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/dbt_valid_to'], name="dbt_valid_to", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/dbt_valid_to'),
                   model_uri=MD_TERMINOLOGY_TROVE.dbt_valid_to, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.display = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/display'], name="display", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/display'),
                   model_uri=MD_TERMINOLOGY_TROVE.display, domain=None, range=Optional[str])

slots.definition = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/definition'], name="definition", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/definition'),
                   model_uri=MD_TERMINOLOGY_TROVE.definition, domain=None, range=Optional[str])

slots.parent_concept_curie = Slot(uri=MD_TERMINOLOGY_TROVE['term-hierarchy-map/parent_concept_curie'], name="parent_concept_curie", curie=MD_TERMINOLOGY_TROVE.curie('term-hierarchy-map/parent_concept_curie'),
                   model_uri=MD_TERMINOLOGY_TROVE.parent_concept_curie, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.mapping_relationship = Slot(uri=MD_TERMINOLOGY_TROVE['term-cross-reference/mapping_relationship'], name="mapping_relationship", curie=MD_TERMINOLOGY_TROVE.curie('term-cross-reference/mapping_relationship'),
                   model_uri=MD_TERMINOLOGY_TROVE.mapping_relationship, domain=None, range=Optional[Union[str, "EnumMappingRelationship"]])

slots.target_concept_curie = Slot(uri=MD_TERMINOLOGY_TROVE['concept-relationship/target_concept_curie'], name="target_concept_curie", curie=MD_TERMINOLOGY_TROVE.curie('concept-relationship/target_concept_curie'),
                   model_uri=MD_TERMINOLOGY_TROVE.target_concept_curie, domain=None, range=Optional[Union[str, ConceptConceptCurie]])

slots.relationship_curie = Slot(uri=MD_TERMINOLOGY_TROVE['concept-relationship/relationship_curie'], name="relationship_curie", curie=MD_TERMINOLOGY_TROVE.curie('concept-relationship/relationship_curie'),
                   model_uri=MD_TERMINOLOGY_TROVE.relationship_curie, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.Vocabulary_vocabulary_id = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/vocabulary_id'], name="Vocabulary_vocabulary_id", curie=MD_TERMINOLOGY_TROVE.curie('ontology/vocabulary_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.Vocabulary_vocabulary_id, domain=Vocabulary, range=Union[str, VocabularyVocabularyId])

slots.Concept_concept_curie = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_curie'], name="Concept_concept_curie", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_curie'),
                   model_uri=MD_TERMINOLOGY_TROVE.Concept_concept_curie, domain=Concept, range=Union[str, ConceptConceptCurie])
