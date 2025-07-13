Quick Start
===========

Install AxiusMEM:

.. code-block:: bash

    pip install axiusmem

Or with conda:

.. code-block:: bash

    conda install -c conda-forge axiusmem

Set Environment Variables
-------------------------

Before running any AxiusMEM code, set the following environment variables so the library can connect to your Jena Fuseki triplestore.

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

See the :doc:`api` for full API reference. 

Available Triplestore Types
---------------------------

The following options are available for the `TRIPLESTORE_TYPE` environment variable:

+----------------+-------------------------------+--------------------------+
| Type           | Description                   | Status                   |
+================+===============================+==========================+
| graphdb        | Ontotext GraphDB              | Implemented              |
| jena           | Apache Jena Fuseki            | Implemented (basic)      |
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
