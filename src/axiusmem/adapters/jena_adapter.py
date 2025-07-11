from .base import BaseTriplestoreAdapter

class JenaAdapter(BaseTriplestoreAdapter):
    """
    Adapter for Apache Jena (TDB/Fuseki) (stub).
    See: https://jena.apache.org/documentation/fuseki2/
    """
    def connect(self):
        """Establish a connection to Jena (not implemented)."""
        raise NotImplementedError("JenaAdapter.connect() not implemented.")

    def close(self):
        """Close the connection to Jena (not implemented)."""
        raise NotImplementedError("JenaAdapter.close() not implemented.")

    def sparql_select(self, query: str, **kwargs):
        """Execute a SPARQL SELECT query on Jena (not implemented)."""
        raise NotImplementedError("JenaAdapter.sparql_select() not implemented.")

    def sparql_update(self, update_query: str, **kwargs):
        """Execute a SPARQL UPDATE query on Jena (not implemented)."""
        raise NotImplementedError("JenaAdapter.sparql_update() not implemented.")

    def bulk_load(self, rdf_path: str, rdf_format: str = "text/turtle"):
        """Bulk load RDF data into Jena (not implemented)."""
        raise NotImplementedError("JenaAdapter.bulk_load() not implemented.")

    def test_connection(self):
        """Test the connection to Jena (not implemented)."""
        raise NotImplementedError("JenaAdapter.test_connection() not implemented.") 