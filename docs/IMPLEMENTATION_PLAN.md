# AxiusMEM Implementation Plan

This document outlines the phased implementation plan for AxiusMEM, a W3C-compliant temporal knowledge graph library for AI agents. Each phase includes clear deliverables and checklists.

---

## Phase 1: Project Foundation & Core RDF Layer

- [x] Scaffold Python package structure (`src/axiusmem/`, setup, requirements, env, etc.)
- [x] Integrate CI/CD basics (lint, test, build, PyPI/conda packaging)
- [x] Add Sphinx documentation skeleton

### RDF Graph Core
- [x] Implement RDF triple store using `rdflib`
- [x] Load and manage OWL ontologies (Turtle, RDF/XML)
- [x] Utilities for extending/updating ontologies at runtime
- [x] Support for RDFS/OWL inferencing (local and GraphDB-backed)
- [x] Entity and relationship definition (programmatic API for classes/properties)
- [x] Data provenance support (PROV-O integration, source/timestamp/agent)

---

## Phase 2: Temporal & Provenance Model

### Bi-Temporal Data Model
- [x] Design and implement valid time (VT) and transaction time (TT) support
  - [x] Use named graphs or reification for TT
  - [x] Use custom or standard properties for VT
- [x] Helper functions for adding/querying temporal intervals
- [x] Point-in-time, as-of, and interval query support

### Provenance
- [x] Attach provenance metadata to triples (source, ingestion time, agent)
- [x] Utilities for querying provenance

---

## Phase 3: Data Ingestion & Update

### Incremental & Batch Ingestion
- [x] Efficiently add/update/delete triples (preserving temporal context)
- [x] Bulk loading utilities (Turtle, N-Triples, RDF/XML)
- [x] Data validation against ontology (SHACL or OWL-based)

### Conflict Resolution
- [x] Implement strategies for temporal/conflicting updates (latest-wins, custom rules)

---

## Phase 4: Query Engine & Retrieval

### SPARQL Query API
- [x] Pythonic API for SELECT, CONSTRUCT, ASK, UPDATE
- [x] Abstract common query patterns (no raw SPARQL needed for basics)
- [x] Support federated queries (if GraphDB allows)

### Temporal Queries
- [x] Point-in-time, as-of, and interval queries (using temporal model)
- [x] Result formatting (Pandas DataFrame, JSON, Python objects)

### Hybrid Search
- [x] Semantic search (vector/embedding-based, GraphDB or external)
- [x] Full-text search (Lucene integration)
- [x] Graph traversal (neighbors, paths, ancestors)
- [x] Combined search (RRF/weighted)

### Explainability
- [x] Mechanisms to explain query results (inference, temporal validity, provenance)

---

## Phase 5: GraphDB Adapter Layer

### Connection & Repository Management
- [x] Connection pooling, secure auth (HTTPS, user/pass, API keys)
- [x] Programmatic repository creation/deletion/configuration
- [x] Repository settings (inference, partitioning)

### Performance & Transactions
- [x] Bulk loading via GraphDB APIs
- [x] Efficient SPARQL query construction
- [x] Transaction management (atomic updates)

---

## Phase 6: Agent Utility Layer

### Agent Context & Memory
- [ ] Simplified APIs for context retrieval (for LLMs/agents)
- [ ] Agent-specific memory storage/retrieval
- [ ] Formatting helpers for LLM prompts

### Dynamic Schema/Ontology Updates
- [ ] Allow agents to propose/incorporate new concepts/relations

---

## Phase 7: ORM/Mapper Layer

- [ ] Map Python objects to RDF and vice versa (common patterns)
- [ ] Support for custom entity/relationship types
- [ ] Easy serialization/deserialization

---

## Phase 8: Non-Functional Requirements

- [ ] Performance benchmarks (ingestion, query latency, scalability)
- [x] Robust error handling and resilience (network, GraphDB outages)
- [x] Security (auth, authorization, secrets management)
- [x] Usability (API clarity, examples, tutorials)
- [x] Maintainability (modular code, tests, docs)
- [x] Portability (future triplestore adapters, clear separation of concerns)

---

## Phase 9: Testing & Documentation

- [x] Unit and integration tests for all modules
- [x] Sphinx-generated API docs
- [x] Example notebooks and tutorials
- [x] Environment and deployment guides

---

## Phase 10: Release & Community

- [ ] PyPI and conda releases
- [ ] Contribution guidelines, code of conduct
- [ ] Issue templates, GitHub discussions
- [ ] Community engagement (examples, feedback, roadmap)

---

### Stretch Goals (Future Phases)
- Adapters for other triplestores (Virtuoso, Stardog, etc.)
- Real-time stream ingestion (Kafka, etc.)
- Advanced temporal analytics and forecasting
- Deeper LLM/AI framework integration (LangChain, LlamaIndex)
- Fine-grained access control 