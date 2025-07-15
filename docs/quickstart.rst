Quick Start
===========

Install AxiusMEM™:

.. code-block:: bash

    pip install axiusmem

Or with conda:

.. code-block:: bash

    conda install -c conda-forge axiusmem

Set Environment Variables
-------------------------

Before running any AxiusMEM™ code, set the following environment variables so the library can connect to your Jena Fuseki triplestore.

**Option 1: Using a .env file (recommended)**

Create a file named `.env` in your project directory with the following contents:

.. code-block:: text

   TRIPLESTORE_TYPE=jena
   TRIPLESTORE_URL=http://localhost:3030
   TRIPLESTORE_USER=admin
   TRIPLESTORE_PASSWORD=yourpassword
   TRIPLESTORE_REPOSITORY=Default

**Option 2: Setting environment variables in your shell**

For **Windows (PowerShell):**

.. code-block:: powershell

   $env:TRIPLESTORE_TYPE="jena"
   $env:TRIPLESTORE_URL="http://localhost:3030"
   $env:TRIPLESTORE_USER="admin"
   $env:TRIPLESTORE_PASSWORD="yourpassword"
   $env:TRIPLESTORE_REPOSITORY="Default"

For **Unix/macOS (bash/zsh):**

.. code-block:: bash

   export TRIPLESTORE_TYPE=jena
   export TRIPLESTORE_URL=http://localhost:3030
   export TRIPLESTORE_USER=admin
   export TRIPLESTORE_PASSWORD=yourpassword
   export TRIPLESTORE_REPOSITORY=Default

Minimal Example:

.. code-block:: python

    from axiusmem import AxiusMEM

    mem = AxiusMEM()
    mem.load_ontology('axiusmem_ontology.ttl')
    mem.connect_graphdb()
    # Add triples, query, manage agent memory, etc.

Jena Fuseki Admin and Dataset Management
---------------------------------------

You can manage datasets and check server status using the following methods on the JenaAdapter:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

   # List all datasets
   datasets = adapter.list_datasets()
   print("Datasets:", datasets)

   # Create a new in-memory dataset
   adapter.create_dataset("mynewdataset", db_type="mem")

   # Delete a dataset
   adapter.delete_dataset("mynewdataset")

   # Get server status
   status = adapter.get_server_status()
   print("Server status:", status)

SPARQL CONSTRUCT, DESCRIBE, and ASK
-----------------------------------

You can use the following methods to run advanced SPARQL queries:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

   # SPARQL CONSTRUCT
   turtle = adapter.sparql_construct("CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o } LIMIT 1")
   print(turtle)

   # SPARQL DESCRIBE
   turtle = adapter.sparql_describe("DESCRIBE <http://example.org/s>")
   print(turtle)

   # SPARQL ASK
   exists = adapter.sparql_ask("ASK { ?s ?p ?o }")
   print(exists)

Dataset Configuration, Backup, and Restore
-----------------------------------------

You can manage dataset configuration and perform backup/restore operations:

.. code-block:: python

   from axiusmem.adapters.base import get_triplestore_adapter_from_env
   adapter = get_triplestore_adapter_from_env()

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

See the :doc:`api` for full API reference. 

Available Triplestore Types
---------------------------

The following options are available for the `TRIPLESTORE_TYPE` environment variable:

+----------------+-------------------------------+--------------------------+
| Type           | Description                   | Status                   |
+================+===============================+==========================+
| graphdb        | Ontotext GraphDB              | Implemented              |
| jena           | Apache Jena Fuseki            | Implemented              |
| allegrograph   | Franz AllegroGraph            | Stub                     |
| anzograph      | Cambridge Semantics AnzoGraph | Stub                     |
| blazegraph     | Blazegraph                    | Stub                     |
| dydra          | Dydra                         | Stub                     |
| fourstore      | 4store                        | Stub                     |
| jena_sdb       | Jena SDB                      | Stub                     |
| marklogic      | MarkLogic                     | Stub                     |
| mulgara        | Mulgara                       | Stub                     |
| neptune        | Amazon Neptune                | Stub                     |
| rdf4j          | Eclipse RDF4J                 | Stub                     |
| rdflib         | RDFLib (local, in-memory)     | Stub                     |
| rdfox          | Oxford Semantic RDFox         | Stub                     |
| redland        | Redland                       | Stub                     |
| redstore       | RedStore                      | Stub                     |
| stardog        | Stardog                       | Stub                     |
| virtuoso       | OpenLink Virtuoso             | Stub                     |
+----------------+-------------------------------+--------------------------+ 
