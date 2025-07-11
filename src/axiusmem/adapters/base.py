class BaseTriplestoreAdapter:
    """
    Abstract base class for all triplestore adapters in AxiusMEM.
    Defines the required interface for RDF store integration.
    """
    def connect(self):
        """Establish a connection to the triplestore."""
        raise NotImplementedError("connect() must be implemented by subclass.")

    def close(self):
        """Close the connection to the triplestore."""
        raise NotImplementedError("close() must be implemented by subclass.")

    def sparql_select(self, query: str, **kwargs):
        """Execute a SPARQL SELECT query."""
        raise NotImplementedError("sparql_select() must be implemented by subclass.")

    def sparql_update(self, update_query: str, **kwargs):
        """Execute a SPARQL UPDATE query."""
        raise NotImplementedError("sparql_update() must be implemented by subclass.")

    def bulk_load(self, rdf_path: str, rdf_format: str = "text/turtle"):
        """Bulk load RDF data into the triplestore."""
        raise NotImplementedError("bulk_load() must be implemented by subclass.")

    def test_connection(self):
        """Test the connection to the triplestore."""
        raise NotImplementedError("test_connection() must be implemented by subclass.") 