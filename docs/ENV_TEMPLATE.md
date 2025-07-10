# =====================
# AxiusMEM .env Template
# =====================

# --- GraphDB / Knowledge Graph ---
AGENT_MEMORY_URL= 
GRAPHDB_USER= 
GRAPHDB_PASSWORD=
GRAPHDB_USE_HTTPS=true

# --- LLM & Embeddings Provider ---
LLM_PROVIDER=openai  # or 'google', etc.
OPENAI_API_KEY=
GOOGLE_API_KEY=
GOOGLE_APPLICATION_CREDENTIALS=
EMBEDDING_MODEL_NAME=text-embedding-ada-002  # or Gemini model name

# --- Vector Store / Index ---
VECTOR_STORE_TYPE=faiss  # or 'annoy', 'pinecone', 'weaviate'
VECTOR_STORE_PATH=./vector_index
PINECONE_API_KEY=
PINECONE_ENVIRONMENT=
PINECONE_INDEX=
WEAVIATE_URL=
WEAVIATE_API_KEY=

# --- Full-Text Search / Elasticsearch ---
ELASTICSEARCH_URL=
ELASTICSEARCH_USER=
ELASTICSEARCH_PASSWORD=

# --- Logging & Debugging ---
LOG_LEVEL=INFO
LOG_FILE=

# --- Application / Agent Metadata ---
AGENT_NAME=SDCKG-Agent
AGENT_ID=agent-001
AGENT_DESCRIPTION=Semantic Data Charter Knowledge Graph Agent

# --- Other Integrations (Optional) ---
KAFKA_BROKER_URL=
REDIS_URL=