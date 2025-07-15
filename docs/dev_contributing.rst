Developer & Contributing Guide
=============================

How to Contribute
-----------------
- Fork the repository and create your branch from `main`.
- Submit pull requests for review.
- Open issues for bugs, feature requests, or questions.
- Join discussions on the GitHub Discussions page.

Adapter Contributions
---------------------
AxiusMEM™ is designed to be extensible for many RDF triplestores. We welcome contributions for any of the following adapters:

- OpenLink Virtuoso
- AllegroGraph (Franz Inc.)
- Amazon Neptune
- Stardog
- MarkLogic
- AnzoGraph DB
- RDFox
- Apache Jena (TDB/Fuseki)
- Eclipse RDF4J
- Blazegraph
- 4store
- Mulgara
- RDFLib
- Redland
- RedStore
- Jena SDB
- Dydra

To contribute an adapter implementation:
- Start from the stub in `src/axiusmem/adapters/` for your triplestore.
- Implement the required methods (`connect`, `close`, `sparql_select`, `sparql_update`, `bulk_load`, `test_connection`).
- Add tests in `tests/`.
- Submit a pull request with your changes and documentation.

Testing
-------
- Run all tests with `pytest` (ensure your environment variables are set for the desired backend).
- Add new tests for any new features or adapters.

Documentation
-------------
- Add or update docstrings and Sphinx documentation for new modules or features.
- Add usage examples for new features.

Your work will help AxiusMEM™ support a wider community of users! 