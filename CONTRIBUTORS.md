# Contributors

Thank you to everyone who has contributed to AxiusMEM™!

- Project Lead: Timothy W. Cook
- Core Developers: [List core devs here]
- Community Contributors: [List community contributors here]

## How to Contribute
- Fork the repository and create your branch from `main`.
- Submit pull requests for review.
- Open issues for bugs, feature requests, or questions.
- Join discussions on the GitHub Discussions page.

All contributions, big or small, are appreciated!

## Triplestore Adapter Contributions
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

Your work will help AxiusMEM™ support a wider community of users! 