# Auto generated from md_terminology_trove.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-29T13:25:54
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

from linkml_runtime.linkml_model.types import Datetime, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

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
class TermOntologyOntologyId(extended_str):
    pass


class TermConceptConceptId(URIorCURIE):
    pass


@dataclass(repr=False)
class HasConceptId(YAMLRoot):
    """
    Base class for all concept tables
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "HasConceptId"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.HasConceptId

    concept_id: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, URIorCURIE):
            self.concept_id = URIorCURIE(self.concept_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermOntology(YAMLRoot):
    """
    Flat table containing each of the ontologies used for dataset annotations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["ontology/TermOntology"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:ontology/TermOntology"
    class_name: ClassVar[str] = "TermOntology"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.TermOntology

    ontology_id: Union[str, TermOntologyOntologyId] = None
    ontology_uri: Union[str, URI] = None
    fhir_system: Union[str, URI] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ontology_id):
            self.MissingRequiredField("ontology_id")
        if not isinstance(self.ontology_id, TermOntologyOntologyId):
            self.ontology_id = TermOntologyOntologyId(self.ontology_id)

        if self._is_empty(self.ontology_uri):
            self.MissingRequiredField("ontology_uri")
        if not isinstance(self.ontology_uri, URI):
            self.ontology_uri = URI(self.ontology_uri)

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

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermConcept(HasConceptId):
    """
    Flat table containing the curied codes for all ontological terms used for dataset annotations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["term-concept/TermConcept"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:term-concept/TermConcept"
    class_name: ClassVar[str] = "TermConcept"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.TermConcept

    concept_id: Union[str, TermConceptConceptId] = None
    ontology_id: Union[str, TermOntologyOntologyId] = None
    dbt_updated_at: Union[str, XSDDateTime] = None
    dbt_valid_from: Union[str, XSDDateTime] = None
    display: Optional[str] = None
    definition: Optional[str] = None
    version: Optional[str] = None
    dbt_valid_to: Optional[Union[str, XSDDateTime]] = None
    dbt_scd_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, TermConceptConceptId):
            self.concept_id = TermConceptConceptId(self.concept_id)

        if self._is_empty(self.ontology_id):
            self.MissingRequiredField("ontology_id")
        if not isinstance(self.ontology_id, TermOntologyOntologyId):
            self.ontology_id = TermOntologyOntologyId(self.ontology_id)

        if self._is_empty(self.dbt_updated_at):
            self.MissingRequiredField("dbt_updated_at")
        if not isinstance(self.dbt_updated_at, XSDDateTime):
            self.dbt_updated_at = XSDDateTime(self.dbt_updated_at)

        if self._is_empty(self.dbt_valid_from):
            self.MissingRequiredField("dbt_valid_from")
        if not isinstance(self.dbt_valid_from, XSDDateTime):
            self.dbt_valid_from = XSDDateTime(self.dbt_valid_from)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.dbt_valid_to is not None and not isinstance(self.dbt_valid_to, XSDDateTime):
            self.dbt_valid_to = XSDDateTime(self.dbt_valid_to)

        if self.dbt_scd_id is not None and not isinstance(self.dbt_scd_id, str):
            self.dbt_scd_id = str(self.dbt_scd_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HierarchyMap(HasConceptId):
    """
    Basic parent/child relationships, suitable for populating a hierarchical FHIR codesystem    is_a: HasConceptId
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["term-hierarchy-map/HierarchyMap"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:term-hierarchy-map/HierarchyMap"
    class_name: ClassVar[str] = "HierarchyMap"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.HierarchyMap

    concept_id: Union[str, TermConceptConceptId] = None
    parent_id: Optional[Union[Union[str, TermConceptConceptId], list[Union[str, TermConceptConceptId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, TermConceptConceptId):
            self.concept_id = TermConceptConceptId(self.concept_id)

        if not isinstance(self.parent_id, list):
            self.parent_id = [self.parent_id] if self.parent_id is not None else []
        self.parent_id = [v if isinstance(v, TermConceptConceptId) else TermConceptConceptId(v) for v in self.parent_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrossReference(HasConceptId):
    """
    References to other terms that are encountered during traversal/loading
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE["term-cross-reference/CrossReference"]
    class_class_curie: ClassVar[str] = "md_terminology_trove:term-cross-reference/CrossReference"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = MD_TERMINOLOGY_TROVE.CrossReference

    concept_id: Union[str, TermConceptConceptId] = None
    target_concept_id: Optional[Union[str, TermConceptConceptId]] = None
    mapping_relationship: Optional[Union[str, "EnumMappingRelationship"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, TermConceptConceptId):
            self.concept_id = TermConceptConceptId(self.concept_id)

        if self.target_concept_id is not None and not isinstance(self.target_concept_id, TermConceptConceptId):
            self.target_concept_id = TermConceptConceptId(self.target_concept_id)

        if self.mapping_relationship is not None and not isinstance(self.mapping_relationship, EnumMappingRelationship):
            self.mapping_relationship = EnumMappingRelationship(self.mapping_relationship)

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

slots.ontology_id = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/ontology_id'], name="ontology_id", curie=MD_TERMINOLOGY_TROVE.curie('ontology/ontology_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.ontology_id, domain=None, range=Union[str, TermOntologyOntologyId])

slots.name = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/name'], name="name", curie=MD_TERMINOLOGY_TROVE.curie('ontology/name'),
                   model_uri=MD_TERMINOLOGY_TROVE.name, domain=None, range=Optional[str])

slots.ontology_uri = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/ontology_uri'], name="ontology_uri", curie=MD_TERMINOLOGY_TROVE.curie('ontology/ontology_uri'),
                   model_uri=MD_TERMINOLOGY_TROVE.ontology_uri, domain=None, range=Union[str, URI])

slots.fhir_system = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/fhir_system'], name="fhir_system", curie=MD_TERMINOLOGY_TROVE.curie('ontology/fhir_system'),
                   model_uri=MD_TERMINOLOGY_TROVE.fhir_system, domain=None, range=Union[str, URI])

slots.prefix = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/prefix'], name="prefix", curie=MD_TERMINOLOGY_TROVE.curie('ontology/prefix'),
                   model_uri=MD_TERMINOLOGY_TROVE.prefix, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z][A-Za-z0-9_\-\.]*$'))

slots.description = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/description'], name="description", curie=MD_TERMINOLOGY_TROVE.curie('ontology/description'),
                   model_uri=MD_TERMINOLOGY_TROVE.description, domain=None, range=Optional[str])

slots.source = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/source'], name="source", curie=MD_TERMINOLOGY_TROVE.curie('ontology/source'),
                   model_uri=MD_TERMINOLOGY_TROVE.source, domain=None, range=Optional[str])

slots.concept_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_id'], name="concept_id", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.concept_id, domain=None, range=Union[str, URIorCURIE])

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

slots.version = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/version'], name="version", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/version'),
                   model_uri=MD_TERMINOLOGY_TROVE.version, domain=None, range=Optional[str])

slots.parent_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-hierarchy-map/parent_id'], name="parent_id", curie=MD_TERMINOLOGY_TROVE.curie('term-hierarchy-map/parent_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.parent_id, domain=None, range=Optional[Union[Union[str, TermConceptConceptId], list[Union[str, TermConceptConceptId]]]])

slots.target_concept_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-cross-reference/target_concept_id'], name="target_concept_id", curie=MD_TERMINOLOGY_TROVE.curie('term-cross-reference/target_concept_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.target_concept_id, domain=None, range=Optional[Union[str, TermConceptConceptId]])

slots.mapping_relationship = Slot(uri=MD_TERMINOLOGY_TROVE['term-cross-reference/mapping_relationship'], name="mapping_relationship", curie=MD_TERMINOLOGY_TROVE.curie('term-cross-reference/mapping_relationship'),
                   model_uri=MD_TERMINOLOGY_TROVE.mapping_relationship, domain=None, range=Optional[Union[str, "EnumMappingRelationship"]])

slots.TermOntology_ontology_id = Slot(uri=MD_TERMINOLOGY_TROVE['ontology/ontology_id'], name="TermOntology_ontology_id", curie=MD_TERMINOLOGY_TROVE.curie('ontology/ontology_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.TermOntology_ontology_id, domain=TermOntology, range=Union[str, TermOntologyOntologyId])

slots.TermConcept_concept_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_id'], name="TermConcept_concept_id", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.TermConcept_concept_id, domain=TermConcept, range=Union[str, TermConceptConceptId])

slots.HierarchyMap_concept_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_id'], name="HierarchyMap_concept_id", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.HierarchyMap_concept_id, domain=HierarchyMap, range=Union[str, TermConceptConceptId])

slots.CrossReference_concept_id = Slot(uri=MD_TERMINOLOGY_TROVE['term-concept/concept_id'], name="CrossReference_concept_id", curie=MD_TERMINOLOGY_TROVE.curie('term-concept/concept_id'),
                   model_uri=MD_TERMINOLOGY_TROVE.CrossReference_concept_id, domain=CrossReference, range=Union[str, TermConceptConceptId])
