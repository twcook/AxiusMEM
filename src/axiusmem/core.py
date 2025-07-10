import rdflib
import os
from dotenv import load_dotenv
from rdflib.namespace import OWL, RDF, RDFS
from typing import List, Tuple, Optional, Union
from .utils import attach_provenance

class AxiusMEM:
    """
    Core class for AxiusMEM: manages RDF graph, ontologies, and entity/relationship definitions.
    """
    def __init__(self, ontology_path: Optional[str] = None, env_path: Optional[str] = None):
        load_dotenv(env_path or ".env")
        self.ontology_path = ontology_path or "docs/axiusmem_ontology.ttl"
        self.graph = rdflib.Graph()
        self.ontologies = set()
        self.load_ontology(self.ontology_path)
        self.graphdb_url = os.getenv("AGENT_MEMORY_URL")
        self.graphdb_user = os.getenv("GRAPHDB_USER")
        self.graphdb_password = os.getenv("GRAPHDB_PASSWORD")
        self.graphdb_https = os.getenv("GRAPHDB_USE_HTTPS", "true").lower() == "true"

    def load_ontology(self, ontology_path: str, format: Optional[str] = None) -> None:
        """
        Load an ontology file (Turtle or RDF/XML) into the graph.
        """
        fmt = format or ("turtle" if ontology_path.endswith(".ttl") else "xml")
        self.graph.parse(ontology_path, format=fmt)
        self.ontologies.add(ontology_path)

    def extend_ontology(self, triples: List[Tuple[rdflib.term.Identifier, rdflib.term.Identifier, rdflib.term.Identifier]]) -> None:
        """
        Add new triples to the ontology at runtime.
        """
        for s, p, o in triples:
            self.graph.add((s, p, o))

    def define_class(self, class_uri: str, label: Optional[str] = None, comment: Optional[str] = None) -> rdflib.URIRef:
        """
        Programmatically define a new RDF class (entity type).
        """
        class_ref = rdflib.URIRef(class_uri)
        self.graph.add((class_ref, RDF.type, OWL.Class))
        if label:
            self.graph.add((class_ref, RDFS.label, rdflib.Literal(label)))
        if comment:
            self.graph.add((class_ref, RDFS.comment, rdflib.Literal(comment)))
        return class_ref

    def define_property(self, prop_uri: str, domain: Optional[str] = None, range_: Optional[str] = None, label: Optional[str] = None, comment: Optional[str] = None) -> rdflib.URIRef:
        """
        Programmatically define a new RDF property (relationship type).
        """
        prop_ref = rdflib.URIRef(prop_uri)
        self.graph.add((prop_ref, RDF.type, OWL.ObjectProperty))
        if domain:
            self.graph.add((prop_ref, RDFS.domain, rdflib.URIRef(domain)))
        if range_:
            self.graph.add((prop_ref, RDFS.range, rdflib.URIRef(range_)))
        if label:
            self.graph.add((prop_ref, RDFS.label, rdflib.Literal(label)))
        if comment:
            self.graph.add((prop_ref, RDFS.comment, rdflib.Literal(comment)))
        return prop_ref

    def add_triples(self, triples: List[Tuple[rdflib.term.Identifier, rdflib.term.Identifier, rdflib.term.Identifier]], provenance: Optional[dict] = None) -> None:
        """
        Add triples to the graph, optionally with provenance.
        """
        for s, p, o in triples:
            self.graph.add((s, p, o))
            if provenance:
                attach_provenance((s, p, o), **provenance)

    def get_graph(self) -> rdflib.Graph:
        """
        Return the underlying rdflib.Graph object.
        """
        return self.graph

    # TODO: Add support for inferencing (local and GraphDB-backed)
    # TODO: Add more provenance utilities as needed 