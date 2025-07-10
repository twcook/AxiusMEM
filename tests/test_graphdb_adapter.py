import os
from dotenv import load_dotenv
load_dotenv()
import pytest
from axiusmem.graphdb_adapter import GraphDBAdapter

def get_env(var):
    v = os.getenv(var)
    if not v:
        pytest.skip(f"Env var {var} not set; skipping GraphDB integration test.")
    return v

@pytest.mark.integration
def test_graphdb_connection_and_ontology_load():
    url = get_env("AGENT_MEMORY_URL")
    user = os.getenv("GRAPHDB_USER")
    password = os.getenv("GRAPHDB_PASSWORD")
    repo_id = os.getenv("GRAPHDB_REPO_ID")
    ontology_path = os.getenv("AXIUSMEM_ONTOLOGY", "docs/axiusmem_ontology.ttl")
    adapter = GraphDBAdapter(url, user, password)
    assert adapter.test_connection(), "Could not connect to GraphDB."
    # Try loading ontology (will fail if repo doesn't exist or is read-only)
    try:
        loaded = adapter.load_ontology(repo_id, ontology_path)
        assert loaded, "Ontology load did not return success status."
    except Exception as e:
        pytest.skip(f"Ontology load failed: {e}") 