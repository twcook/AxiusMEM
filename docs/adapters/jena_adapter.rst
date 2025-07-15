JenaAdapter
===========

The JenaAdapter provides integration with Apache Jena Fuseki.

Status: **Implemented**

Supported Features:
- SPARQL SELECT/UPDATE
- SPARQL CONSTRUCT/DESCRIBE/ASK
- Bulk load RDF
- Test connection
- Dataset (repository) management (list, create, delete, config, backup, restore)
- Server status

All adapters inherit from the `BaseTriplestoreAdapter` and are instantiated via the factory function:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

The dataset is set via the `TRIPLESTORE_REPOSITORY` environment variable or at adapter initialization.

Environment Variables:
- TRIPLESTORE_TYPE=jena
- TRIPLESTORE_URL (e.g., http://localhost:3030)
- TRIPLESTORE_USER (optional)
- TRIPLESTORE_PASSWORD (optional)
- TRIPLESTORE_REPOSITORY (dataset name)

Example Usage:

.. code-block:: python

   # Get dataset config
   config = adapter.get_dataset_config("Default")
   print(config)

   # Set dataset config (example: change label)
   config["label"] = "New Label"
   adapter.set_dataset_config("Default", config)

   # Backup a dataset
   adapter.backup_dataset("Default", "Default-backup.zip")

   # Restore a dataset
   adapter.restore_dataset("Default", "Default-backup.zip")

   # SPARQL CONSTRUCT
   turtle = adapter.sparql_construct("CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o } LIMIT 1")
   print(turtle)

   # SPARQL DESCRIBE
   turtle = adapter.sparql_describe("DESCRIBE <http://example.org/s>")
   print(turtle)

   # SPARQL ASK
   exists = adapter.sparql_ask("ASK { ?s ?p ?o }")
   print(exists)

   # List datasets
   print(adapter.list_datasets())

   # Create a dataset
   adapter.create_dataset("mydataset", db_type="mem")

   # Delete a dataset
   adapter.delete_dataset("mydataset")

   # Get server status
   print(adapter.get_server_status())

   # SPARQL SELECT
   print(adapter.sparql_select("SELECT * WHERE { ?s ?p ?o } LIMIT 1"))

See the API reference for full method documentation. 