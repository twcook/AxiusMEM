ORM Utilities
=============

AxiusMEM provides ORM-like helpers to map Python dataclasses or dicts to RDF triples and vice versa, define entity/relationship types, and serialize/deserialize objects.

Overview
--------
- Map Python dataclasses or dicts to RDF triples.
- Map RDF resources back to Python dicts.
- Define new entity and relationship types in the ontology.
- Serialize/deserialize objects to/from RDF.

Example Usage
-------------

.. code-block:: python

   import dataclasses
   from rdflib import Graph
   from axiusmem.orm import (
       object_to_rdf, rdf_to_object,
       define_entity_type, define_relationship_type,
       serialize_object, deserialize_object, EX
   )

   @dataclasses.dataclass
   class Person:
       name: str
       age: int

   g = Graph()

   # Map a dataclass to RDF
   s = object_to_rdf(Person("Alice", 30), g, class_uri=EX.Person)

   # Map RDF back to dict
   obj = rdf_to_object(g, s)

   # Define a new entity type
   device_class = define_entity_type(g, "SmartDevice")

   # Define a new relationship type
   controls = define_relationship_type(g, "controls", EX.Agent, EX.Device)

   # Serialize a Python object to RDF Turtle
   rdf_str = serialize_object({"name": "Alice", "age": 30}, format="turtle")

   # Deserialize RDF to Python dicts
   objs = deserialize_object(rdf_str, format="turtle")

See the API reference for full method documentation. 