# AxiusMEM

A W3C-compliant temporal knowledge graph library for AI agents.

[![PyPI version](https://badge.fury.io/py/axiusmem.svg)](https://badge.fury.io/py/axiusmem)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://readthedocs.org/projects/axiusmem/badge/?version=latest)](https://axiusmem.readthedocs.io/en/latest/)

## Features
- **Bi-temporal data model** (valid & transaction time)
- **Incremental and batch data ingestion**
- **Advanced querying** (SPARQL, temporal, semantic, full-text)
- **GraphDB integration** (connection pooling, repository management)
- **AI agent utilities** (context retrieval, memory management)
- **ORM/Mapper** (Python objects <-> RDF)
- **Extensive tests and Sphinx documentation**

## Installation

### Using pip
```bash
pip install axiusmem
```

### Using conda
```bash
conda install -c conda-forge axiusmem
```

## Quick Start
```python
from axiusmem import AxiusMEM

mem = AxiusMEM()
mem.load_ontology('src/axiusmem/axiusmem_ontology.ttl')
mem.connect_graphdb()
# Add triples, query, manage agent memory, etc.
```

## Documentation
- [Sphinx Docs (HTML)](https://axiusmem.readthedocs.io/en/latest/)
- [Product Requirements (PRD)](docs/PRD_%20AxiusMEM.md)
- [Ontology (Turtle)](src/axiusmem/axiusmem_ontology.ttl)
- [Developer Guide](docs/docs_dev_guide.md)

## Contributing
See [CONTRIBUTORS.md](CONTRIBUTORS.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## License
See [LICENSE](LICENSE).

## Community & Support
- Feedback, issues, and feature requests: [GitHub Issues](https://github.com/your-org/axiusmem/issues)
- Roadmap and discussions: [GitHub Discussions](https://github.com/your-org/axiusmem/discussions) 

## Triplestore Configuration

AxiusMEM now supports generic configuration for multiple triplestores. Set the following environment variables:

- `TRIPLESTORE_TYPE`: The type of triplestore to use (`graphdb`, `jena`, etc.)
- `TRIPLESTORE_URL`: The base URL or host for the triplestore
- `TRIPLESTORE_USER`: Username for authentication (optional)
- `TRIPLESTORE_PASSWORD`: Password for authentication (optional)
- `TRIPLESTORE_REPOSITORY`: Repository or dataset name (if required by the backend)

Example for GraphDB:
```
TRIPLESTORE_TYPE=graphdb
TRIPLESTORE_URL=http://localhost:7200
TRIPLESTORE_USER=admin
TRIPLESTORE_PASSWORD=secret
TRIPLESTORE_REPOSITORY=myrepo
```

Example for Jena Fuseki:
```
TRIPLESTORE_TYPE=jena
TRIPLESTORE_URL=http://localhost:3030
TRIPLESTORE_USER=admin
TRIPLESTORE_PASSWORD=secret
TRIPLESTORE_REPOSITORY=Default
```

## Adapter Factory Usage

To obtain the correct adapter for your environment, use:

```python
from axiusmem.adapters.base import get_triplestore_adapter_from_env
adapter = get_triplestore_adapter_from_env()
```

This will automatically select and configure the appropriate adapter based on your environment variables. 

# Jena Fuseki Adapter Usage

AxiusMEM now provides first-class support for Apache Jena Fuseki as a triplestore backend. Below are detailed setup and usage instructions.

## Environment Variable Setup

Set the following environment variables to configure AxiusMEM to use Jena Fuseki:

- `TRIPLESTORE_TYPE=jena`
- `TRIPLESTORE_URL=http://localhost:3030`  # Change host/port as needed
- `TRIPLESTORE_USER=admin`                 # Your Fuseki username (if required)
- `TRIPLESTORE_PASSWORD=yourpassword`      # Your Fuseki password (if required)
- `TRIPLESTORE_REPOSITORY=Default`         # The dataset name in your Fuseki server

You can set these in your shell, a `.env` file, or your environment manager.

## Example: .env File
```
TRIPLESTORE_TYPE=jena
TRIPLESTORE_URL=http://localhost:3030
TRIPLESTORE_USER=admin
TRIPLESTORE_PASSWORD=yourpassword
TRIPLESTORE_REPOSITORY=Default
```

## Using the Adapter in Code

```python
from axiusmem.adapters.base import get_triplestore_adapter_from_env
adapter = get_triplestore_adapter_from_env()

# Example: Run a SPARQL SELECT query
query = "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"
results = adapter.sparql_select(query)
print(results)

# Example: Run a SPARQL UPDATE
update = "INSERT DATA { <http://example.org/s> <http://example.org/p> <http://example.org/o> }"
adapter.sparql_update(update)

# Example: Bulk load RDF data
adapter.bulk_load("mydata.ttl", rdf_format="text/turtle")

# Test the connection
if adapter.test_connection():
    print("Jena Fuseki connection successful!")
else:
    print("Failed to connect to Jena Fuseki.")
```

## Troubleshooting & Common Issues

- **Connection Refused:** Ensure your Jena Fuseki server is running and accessible at the URL you provided.
- **Authentication Errors:** Double-check your username and password. If authentication is not required, leave these variables blank.
- **Dataset Not Found:** Make sure the dataset name in `TRIPLESTORE_REPOSITORY` matches one configured in your Fuseki server.
- **SPARQL Errors:** Check your query syntax and ensure your dataset contains data.

## Verifying Jena Fuseki is Running
- Visit `http://localhost:3030` in your browser. You should see the Fuseki web interface.
- Use the Fuseki UI to create datasets, upload data, and test queries.

## Extending to Other Triplestores
While this documentation focuses on Jena Fuseki, AxiusMEM is designed to support other triplestores via the adapter factory. To use another backend, set `TRIPLESTORE_TYPE` and the relevant environment variables, and ensure the adapter is implemented. 
