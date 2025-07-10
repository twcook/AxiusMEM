import requests

class GraphDBAdapter:
    def __init__(self, url, user=None, password=None, use_https=True):
        self.url = url.rstrip('/')
        self.user = user
        self.password = password
        self.use_https = use_https
        self.session = requests.Session()
        if user and password:
            self.session.auth = (user, password)

    def test_connection(self):
        """
        Test connection to GraphDB by listing repositories.
        Returns True if successful, False otherwise.
        """
        try:
            resp = self.session.get(f"{self.url}/rest/repositories")
            resp.raise_for_status()
            return True
        except Exception as e:
            print(f"GraphDB connection failed: {e}")
            return False

    def load_ontology(self, repo_id, ontology_path):
        """
        Load ontology data (Turtle) into the specified repository using SPARQL UPDATE.
        """
        with open(ontology_path, "r", encoding="utf-8") as f:
            turtle_data = f.read()
        update_query = f"""
        INSERT DATA {{
        {turtle_data}
        }}
        """
        endpoint = f"{self.url}/repositories/{repo_id}/statements"
        headers = {"Content-Type": "application/sparql-update"}
        resp = self.session.post(endpoint, data=update_query.encode("utf-8"), headers=headers)
        resp.raise_for_status()
        return resp.status_code == 204 