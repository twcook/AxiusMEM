.. AxiusMEM™ documentation master file, created by
   sphinx-quickstart on Fri Jun 14 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AxiusMEM™'s documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   api
   adapters/index
   temporal
   agent_memory
   orm
   dev_contributing

Adapters
--------

AxiusMEM™ supports a variety of triplestore backends via adapters. See the documentation for each adapter for details, usage, and implementation status:

- :doc:`adapters/jena_adapter`
- :doc:`adapters/graphdb_adapter`
- :doc:`adapters/allegrograph_adapter`
- :doc:`adapters/anzograph_adapter`
- :doc:`adapters/blazegraph_adapter`
- :doc:`adapters/dydra_adapter`
- :doc:`adapters/fourstore_adapter`
- :doc:`adapters/jena_sdb_adapter`
- :doc:`adapters/marklogic_adapter`
- :doc:`adapters/mulgara_adapter`
- :doc:`adapters/neptune_adapter`
- :doc:`adapters/rdf4j_adapter`
- :doc:`adapters/rdflib_adapter`
- :doc:`adapters/rdfox_adapter`
- :doc:`adapters/redland_adapter`
- :doc:`adapters/redstore_adapter`
- :doc:`adapters/stardog_adapter`
- :doc:`adapters/virtuoso_adapter`

Implemented adapters have full usage documentation. Stub adapters are not yet implemented and will raise NotImplementedError if used.

Jena Fuseki Adapter Usage
-------------------------
AxiusMEM™ provides first-class support for Apache Jena Fuseki as a triplestore backend.

**Environment Variables:**

- ``TRIPLESTORE_TYPE=jena``
- ``TRIPLESTORE_URL=http://localhost:3030``
- ``TRIPLESTORE_USER=admin`` (if required)
- ``TRIPLESTORE_PASSWORD=yourpassword`` (if required)
- ``TRIPLESTORE_REPOSITORY=Default``

**Example Usage:**

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

   # SPARQL SELECT
   query = "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"
   results = adapter.sparql_select(query)
   print(results)

   # SPARQL UPDATE
   update = "INSERT DATA { <http://example.org/s> <http://example.org/p> <http://example.org/o> }"
   adapter.sparql_update(update)

   # Bulk load RDF
   adapter.bulk_load("mydata.ttl", rdf_format="text/turtle")

   # Test connection
   if adapter.test_connection():
       print("Jena Fuseki connection successful!")
   else:
       print("Failed to connect to Jena Fuseki.")

**Troubleshooting:**

- Ensure your Jena Fuseki server is running and accessible.
- Double-check credentials and dataset name.
- Visit ``http://localhost:3030`` to verify the server is up.

JenaAdapter API
---------------

(See the API Reference section for full details on JenaAdapter methods.)

Adapter Factory
---------------

(See the API Reference section for full details on the adapter factory.) 