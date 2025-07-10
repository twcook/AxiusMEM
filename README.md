# AxiusMEM

A W3C-compliant temporal knowledge graph library for AI agents.

## Overview
AxiusMEM empowers AI agents with a dynamic, standards-based knowledge base supporting temporal reasoning, continuous learning, and advanced querying. It is optimized for Ontotext GraphDB and strictly adheres to RDF, SPARQL, and OWL standards.

- **Bi-temporal data model** (valid & transaction time)
- **Incremental and batch data ingestion**
- **Advanced querying** (SPARQL, temporal, semantic, full-text)
- **GraphDB integration** (connection pooling, repository management)
- **AI agent utilities** (context retrieval, memory management)

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
mem.load_ontology('docs/axiusmem_ontology.ttl')
mem.connect_graphdb()
# Add triples, query, manage agent memory, etc.
```

## Documentation
See [docs/PRD_ AxiusMEM.md](docs/PRD_%20AxiusMEM.md) for requirements and [docs/axiusmem_ontology.ttl](docs/axiusmem_ontology.ttl) for the ontology.

## License
See LICENSE. 
