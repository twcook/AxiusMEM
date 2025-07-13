GraphDBAdapter
==============

The GraphDBAdapter provides integration with Ontotext GraphDB.

Status: **Implemented**

Supported Features:
- SPARQL SELECT/UPDATE/CONSTRUCT/ASK
- Bulk load RDF
- Test connection
- Repository management (list, create, delete, configure)
- Advanced features: Lucene search, vector search, transactions, federated queries

Environment Variables:
- TRIPLESTORE_TYPE=graphdb
- TRIPLESTORE_URL (e.g., http://localhost:7200)
- TRIPLESTORE_USER (optional)
- TRIPLESTORE_PASSWORD (optional)
- TRIPLESTORE_REPOSITORY (repository name)

Example Usage:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

   # List repositories
   print(adapter.list_repositories())

   # SPARQL SELECT
   print(adapter.sparql_select("myrepo", "SELECT * WHERE { ?s ?p ?o } LIMIT 1"))

See the API reference for full method documentation. 