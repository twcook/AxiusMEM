.. AxiusMEM documentation master file, created by
   sphinx-quickstart on Fri Jun 14 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AxiusMEM's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   quickstart

Jena Fuseki Adapter Usage
-------------------------
AxiusMEM provides first-class support for Apache Jena Fuseki as a triplestore backend.

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