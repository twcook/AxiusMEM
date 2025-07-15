Adapters
========

AxiusMEM™ provides a unified interface for triplestore integration via the `BaseTriplestoreAdapter` abstract base class. All concrete adapters inherit from this base class and implement the required methods for SPARQL queries, updates, bulk loading, transactions, and named graph management (where supported).

**Adapter Factory:**

The recommended way to instantiate an adapter is via the factory function:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

This will automatically select and configure the correct adapter based on environment variables (see each adapter's documentation for details).

Supported Adapters:

.. toctree::
   :maxdepth: 1

   jena_adapter
   graphdb_adapter
   allegrograph_adapter
   anzograph_adapter
   blazegraph_adapter
   dydra_adapter
   fourstore_adapter
   jena_sdb_adapter
   marklogic_adapter
   mulgara_adapter
   neptune_adapter
   rdf4j_adapter
   rdflib_adapter
   rdfox_adapter
   redland_adapter
   redstore_adapter
   stardog_adapter
   virtuoso_adapter 