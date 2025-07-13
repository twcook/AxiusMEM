import requests
from requests.auth import HTTPBasicAuth
from .base import BaseTriplestoreAdapter

class JenaAdapter(BaseTriplestoreAdapter):
    """
    Adapter for Apache Jena (TDB/Fuseki).
    Connects to a Fuseki server via HTTP.
    """
    def __init__(self, host='localhost', port=3030, dataset='Default', username=None, password=None, protocol='http'):
        self.host = host
        self.port = port
        self.dataset = dataset
        self.username = username
        self.password = password
        self.protocol = protocol
        self.session = None
        self.base_url = None

    def connect(self):
        """Establish a connection to Jena Fuseki (sets up session and base URL)."""
        self.base_url = f"{self.protocol}://{self.host}:{self.port}/{self.dataset}"
        self.session = requests.Session()
        if self.username and self.password:
            self.session.auth = HTTPBasicAuth(self.username, self.password)

    def close(self):
        """Close the session to Jena Fuseki."""
        if self.session:
            self.session.close()
            self.session = None

    def sparql_select(self, query: str, **kwargs):
        """Execute a SPARQL SELECT query on Jena Fuseki."""
        if not self.session:
            self.connect()
        endpoint = f"{self.base_url}/sparql"
        headers = {'Accept': 'application/sparql-results+json'}
        data = {'query': query}
        response = self.session.post(endpoint, data=data, headers=headers, timeout=kwargs.get('timeout', 30))
        response.raise_for_status()
        return response.json()

    def sparql_update(self, update_query: str, **kwargs):
        """Execute a SPARQL UPDATE query on Jena Fuseki."""
        if not self.session:
            self.connect()
        endpoint = f"{self.base_url}/update"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'update': update_query}
        response = self.session.post(endpoint, data=data, headers=headers, timeout=kwargs.get('timeout', 30))
        response.raise_for_status()
        return response.text

    def bulk_load(self, rdf_path: str, rdf_format: str = "text/turtle"):
        """Bulk load RDF data into Jena Fuseki using the /data endpoint."""
        if not self.session:
            self.connect()
        endpoint = f"{self.base_url}/data"
        headers = {'Content-Type': rdf_format}
        with open(rdf_path, 'rb') as f:
            data = f.read()
        response = self.session.post(endpoint, data=data, headers=headers)
        response.raise_for_status()
        return response.text

    def test_connection(self):
        """Test the connection to Jena Fuseki by running a simple ASK query."""
        try:
            result = self.sparql_select("ASK {}")
            return result.get('boolean', False)
        except Exception as e:
            return False 
        