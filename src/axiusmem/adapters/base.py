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


def get_triplestore_adapter_from_env():
    """
    Factory to instantiate the correct triplestore adapter based on environment variables.

    Reads:
        TRIPLESTORE_TYPE: 'graphdb', 'jena', etc.
        TRIPLESTORE_URL: base URL or host
        TRIPLESTORE_USER: username (optional)
        TRIPLESTORE_PASSWORD: password (optional)
        TRIPLESTORE_REPOSITORY: repository or dataset name (optional)

    Returns:
        An instance of the appropriate triplestore adapter.

    Raises:
        ValueError: If TRIPLESTORE_TYPE is unknown or required variables are missing.
    """
    import os
    ttype = os.getenv("TRIPLESTORE_TYPE", "graphdb").lower()
    url = os.getenv("TRIPLESTORE_URL")
    user = os.getenv("TRIPLESTORE_USER")
    password = os.getenv("TRIPLESTORE_PASSWORD")
    repo = os.getenv("TRIPLESTORE_REPOSITORY")
    # Import adapters here to avoid circular imports
    from axiusmem.graphdb_adapter import GraphDBAdapter
    from axiusmem.adapters.jena_adapter import JenaAdapter
    # Add more imports as adapters are implemented
    if ttype == "graphdb":
        if not url:
            raise ValueError("TRIPLESTORE_URL must be set for GraphDB.")
        return GraphDBAdapter(url, user, password)
    elif ttype == "jena":
        if not url or not repo:
            raise ValueError("TRIPLESTORE_URL and TRIPLESTORE_REPOSITORY must be set for Jena.")
        # Parse host/port from url if needed
        import re
        m = re.match(r"https?://([^:/]+)(?::(\d+))?", url)
        host = m.group(1) if m else url
        port = int(m.group(2)) if m and m.group(2) else 3030
        protocol = "https" if url.startswith("https://") else "http"
        return JenaAdapter(host=host, port=port, dataset=repo, username=user, password=password, protocol=protocol)
    else:
        raise ValueError(f"Unknown TRIPLESTORE_TYPE: {ttype}") 