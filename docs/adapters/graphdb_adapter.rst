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

All adapters inherit from the `BaseTriplestoreAdapter` and are instantiated via the factory function:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

The repository is set via the `TRIPLESTORE_REPOSITORY` environment variable or at adapter initialization.

Environment Variables:
- TRIPLESTORE_TYPE=graphdb
- TRIPLESTORE_URL (e.g., http://localhost:7200)
- TRIPLESTORE_USER (optional)
- TRIPLESTORE_PASSWORD (optional)
- TRIPLESTORE_REPOSITORY (repository name)

Example Usage:

.. code-block:: python

   # List repositories
   print(adapter.list_repositories())

   # SPARQL SELECT (uses the repository set at init or via env)
   print(adapter.sparql_select("SELECT * WHERE { ?s ?p ?o } LIMIT 1"))

See the API reference for full method documentation. 