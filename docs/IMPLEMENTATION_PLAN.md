# AxiusMEM Implementation Plan

This document outlines the phased implementation plan for AxiusMEM, a W3C-compliant temporal knowledge graph library for AI agents. Each phase includes clear deliverables and checklists.

---

## Phase 1: Project Foundation & Core RDF Layer

- [x] Scaffold Python package structure (`src/axiusmem/`, setup, requirements, env, etc.)
- [x] Integrate CI/CD basics (lint, test, build, PyPI/conda packaging)
- [x] Add Sphinx documentation skeleton

### RDF Graph Core
- [ ] Implement RDF triple store using `rdflib`
- [ ] Load and manage OWL ontologies (Turtle, RDF/XML)
- [ ] Utilities for extending/updating ontologies at runtime
- [ ] Support for RDFS/OWL inferencing (local and GraphDB-backed)
- [ ] Entity and relationship definition (programmatic API for classes/properties)
- [ ] Data provenance support (PROV-O integration, source/timestamp/agent)

---

## Phase 2: Temporal & Provenance Model

### Bi-Temporal Data Model
- [ ] Design and implement valid time (VT) and transaction time (TT) support
  - Use named graphs or reification for TT
  - Use custom or standard properties for VT
- [ ] Helper functions for adding/querying temporal intervals
- [ ] Point-in-time, as-of, and interval query support

### Provenance
- [ ] Attach provenance metadata to triples (source, ingestion time, agent)
- [ ] Utilities for querying provenance

---

## Phase 3: Data Ingestion & Update

### Incremental & Batch Ingestion
- [ ] Efficiently add/update/delete triples (preserving temporal context)
- [ ] Bulk loading utilities (Turtle, N-Triples, RDF/XML)
- [ ] Data validation against ontology (SHACL or OWL-based)

### Conflict Resolution
- [ ] Implement strategies for temporal/conflicting updates (latest-wins, custom rules)

---

## Phase 4: Query Engine & Retrieval

### SPARQL Query API
- [ ] Pythonic API for SELECT, CONSTRUCT, ASK, UPDATE
- [ ] Abstract common query patterns (no raw SPARQL needed for basics)
- [ ] Support federated queries (if GraphDB allows)

### Temporal Queries
- [ ] Point-in-time, as-of, and interval queries (using temporal model)
- [ ] Result formatting (Pandas DataFrame, JSON, Python objects)

### Hybrid Search
- [ ] Semantic search (vector/embedding-based, GraphDB or external)
- [ ] Full-text search (Lucene integration)
- [ ] Graph traversal (neighbors, paths, ancestors)
- [ ] Combined search (RRF/weighted)

### Explainability
- [ ] Mechanisms to explain query results (inference, temporal validity, provenance)

---

## Phase 5: GraphDB Adapter Layer

### Connection & Repository Management
- [ ] Connection pooling, secure auth (HTTPS, user/pass, API keys)
- [ ] Programmatic repository creation/deletion/configuration
- [ ] Repository settings (inference, partitioning)

### Performance & Transactions
- [ ] Bulk loading via GraphDB APIs
- [ ] Efficient SPARQL query construction
- [ ] Transaction management (atomic updates)

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
- [ ] Robust error handling and resilience (network, GraphDB outages)
- [ ] Security (auth, authorization, secrets management)
- [ ] Usability (API clarity, examples, tutorials)
- [ ] Maintainability (modular code, tests, docs)
- [ ] Portability (future triplestore adapters, clear separation of concerns)

---

## Phase 9: Testing & Documentation

- [ ] Unit and integration tests for all modules
- [ ] Sphinx-generated API docs
- [ ] Example notebooks and tutorials
- [ ] Environment and deployment guides

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