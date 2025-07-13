Temporal and Provenance Features
==============================

AxiusMEM supports bi-temporal RDF data, allowing you to attach and query both valid time and transaction time for triples. This enables point-in-time, as-of, and interval-based temporal reasoning.

Overview
--------
- Attach valid time and transaction time to RDF triples using reification.
- Query for triples valid at a specific time, as of a transaction time, or within an interval.

Example Usage
-------------

.. code-block:: python

   from rdflib import Graph, URIRef, Literal
   from axiusmem.temporal import (
       add_valid_time, add_transaction_time,
       query_point_in_time, query_as_of,
       query_interval_valid_time, query_interval_transaction_time
   )

   g = Graph()
   s, p, o = URIRef("s"), URIRef("p"), Literal("o")

   # Attach valid time
   add_valid_time(g, (s, p, o), valid_from="2024-01-01", valid_to="2024-12-31")

   # Attach transaction time
   add_transaction_time(g, (s, p, o), transaction_from="2024-01-01")

   # Query for triples valid at a specific time
   subgraph = query_point_in_time(g, "2024-06-01")

   # Query for triples as of a transaction time
   as_of_graph = query_as_of(g, "2024-07-01")

See the API reference for full method documentation. 