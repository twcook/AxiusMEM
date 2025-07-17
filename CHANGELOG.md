# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-07-01
### Added
- Initial public release of AxiusMEM™
- RDF triple store, temporal model, ingestion, querying, and agent utilities
- GraphDB adapter (full), scaffolds for 16+ triplestore adapters
- ORM/Mapper layer for Python <-> RDF
- Sphinx documentation, quickstart, and API reference
- Comprehensive tests and benchmarking suite
- Community files: README, CONTRIBUTORS, CODE_OF_CONDUCT
- GitHub issue and PR templates
- Example Jupyter notebook 

## [1.2.0] - 2025-07-14

### Added
- New notebooks for quickstart for Jena and GraphDB
- Fixed module bug in adapters

## [1.2.1] - 2025-07-16

### Updated Notebooks
- Quickstart notebook now uses the new `get_default_ontology_path` function
- Quickstart notebook now uses the new `load_default_ontology` function
- Quickstart notebook now works with the axiusmem ontology
- Quickstart notebook now works with temporal model

## [1.3.0] - 2025-07-17

### Added
- First-class support for Apache Jena Fuseki as a triplestore backend (JenaAdapter)
- Generic triplestore configuration via environment variables (`TRIPLESTORE_TYPE`, `TRIPLESTORE_URL`, etc.)
- REST API for user and role management (admin/agent roles, JWT authentication)
- Admin-only endpoints for metrics, tasks, transactions, and named graph management
- Public SPARQL endpoint for read-only queries
- Automatic retry policy for triplestore/network operations (with exponential backoff)
- Improved error handling and user-facing error messages
- Enhanced server statistics and logging (uptime, request counts, auth success/failure)
- Updated ontology with user/role classes and properties
- Updated and expanded documentation and quickstart guides
- New and updated Jupyter notebooks for quickstart and API integration

### Changed
- Refactored adapter layer to use a unified BaseTriplestoreAdapter interface
- Updated dependency versions and added new dependencies for API features
- License changed to Apache-2.0

### Fixed
- Various bug fixes and documentation improvements

