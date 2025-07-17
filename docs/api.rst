API Reference
=============

JenaAdapter
-----------
.. autoclass:: axiusmem.adapters.jena_adapter.JenaAdapter
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Adapter Factory
---------------
.. autofunction:: axiusmem.adapters.base.get_triplestore_adapter_from_env
   :no-index: 

.. _user_role_api:

User and Role Management REST API
=================================

AxiusMEM™ provides a REST API for user and role management, supporting admin and agent roles.

Features
--------
- Admin endpoints: create/delete users, assign roles, list users
- Agent endpoints: authenticate, get own info/roles
- JWT-based authentication
- Only admins can manage users/roles

Quick Start
-----------

1. Install dependencies::

    pip install fastapi uvicorn bcrypt python-jose

2. Run the API server::

    uvicorn src.axiusmem.api:app --reload

3. Use the interactive docs at http://localhost:8000/docs

Example Usage
-------------

- **Authenticate (get JWT):**

  .. code-block:: bash

     curl -X POST "http://localhost:8000/token" -d 'username=admin&password=yourpassword' -H 'Content-Type: application/x-www-form-urlencoded'

- **Create user (admin only):**

  .. code-block:: bash

     curl -X POST "http://localhost:8000/users/?username=alice&password=secret&roles=agent" -H "Authorization: Bearer <JWT>"

- **Get current user info:**

  .. code-block:: bash

     curl -H "Authorization: Bearer <JWT>" http://localhost:8000/me

See the OpenAPI docs for all endpoints and details. 

.. _server_stats:

Server Logs and Statistics
=========================

AxiusMEM™ tracks server statistics and logs all API requests and responses. Admins can access live server stats via a dedicated endpoint.

Features
--------
- Logs every API request and response (method, path, status)
- Tracks uptime, total requests, per-endpoint counts, auth success/failure, and user count
- In-memory stats (reset on server restart)
- Admin-only ``/server/stats`` endpoint returns all stats as JSON

Example: Get Server Stats
-------------------------

1. Authenticate as admin to get a JWT token::

    curl -X POST "http://localhost:8000/token" -d 'username=admin&password=yourpassword' -H 'Content-Type: application/x-www-form-urlencoded'
    # Response: { "access_token": "...", "token_type": "bearer" }

2. Query server stats::

    curl -H "Authorization: Bearer <JWT>" http://localhost:8000/server/stats
    # Example response:
    # {
    #   "uptime_seconds": 123,
    #   "total_requests": 42,
    #   "endpoint_counts": {"/token": 5, "/users/": 10, ...},
    #   "auth_success": 4,
    #   "auth_failure": 1,
    #   "user_count": 3
    # }

See logs in your console or log file for detailed request/response info. 

.. _transactions_api:

Transactions API
===============

AxiusMEM™ provides admin-only endpoints for triplestore transactions (begin, commit, rollback) if supported by the backend adapter.

Endpoints
---------
- ``POST /transactions/begin`` → returns a transaction ID (tx_id)
- ``POST /transactions/{tx_id}/commit`` → commits the transaction
- ``POST /transactions/{tx_id}/rollback`` → rolls back the transaction

**Note:** Not all adapters support transactions. If not supported, a 501 error is returned.

Example Usage
-------------

1. Begin a transaction::

    curl -X POST -H "Authorization: Bearer <JWT>" http://localhost:8000/transactions/begin
    # Response: { "tx_id": "..." }

2. Commit the transaction::

    curl -X POST -H "Authorization: Bearer <JWT>" http://localhost:8000/transactions/<tx_id>/commit
    # Response: { "msg": "Transaction <tx_id> committed." }

3. Rollback the transaction::

    curl -X POST -H "Authorization: Bearer <JWT>" http://localhost:8000/transactions/<tx_id>/rollback
    # Response: { "msg": "Transaction <tx_id> rolled back." }

See the OpenAPI docs for details and adapter support. 

.. _transactions_api_tests:

Transaction API Tests
====================

AxiusMEM™ includes automated tests for the transaction API endpoints. These tests:

- Verify that `POST /transactions/begin` returns a transaction ID if supported, or a 501 error if not.
- Verify that `POST /transactions/{tx_id}/commit` and `/rollback` succeed for supported adapters.
- Are skipped for unsupported adapters, or check for the correct error response.

**How to interpret results:**
- If your adapter supports transactions (e.g., GraphDB), the tests will check the full lifecycle (begin, commit, rollback).
- If your adapter does not support transactions (e.g., Jena), the tests will confirm that a 501 error is returned.

See `tests/test_api.py` for details and to extend coverage. 

.. _named_graph_api:

Named Graph Management API
=========================

AxiusMEM™ provides admin-only endpoints for managing named graphs (if supported by the backend adapter).

Endpoints
---------
- ``GET /graphs/`` — list all named graphs
- ``POST /graphs/`` — create a named graph (body: ``{"graph_uri": "..."}``)
- ``DELETE /graphs/{graph_uri}`` — delete a named graph
- ``POST /graphs/{graph_uri}/clear`` — clear all triples from a named graph
- ``POST /graphs/{graph_uri}/add`` — add triples to a named graph (body: ``{"triples": [[s, p, o], ...]}``)
- ``POST /graphs/{graph_uri}/query`` — run a SPARQL query against a named graph (body: ``{"query": "..."}``)

**Note:** Not all adapters support named graphs. If not supported, a 501 error is returned.

Example Usage
-------------

1. List named graphs::

    curl -H "Authorization: Bearer <JWT>" http://localhost:8000/graphs/
    # Response: { "graphs": ["http://example.org/graph1", ...] }

2. Create a named graph::

    curl -X POST -H "Authorization: Bearer <JWT>" -H "Content-Type: application/json" \
      -d '{"graph_uri": "http://example.org/graph1"}' http://localhost:8000/graphs/
    # Response: { "msg": "Named graph http://example.org/graph1 created." }

3. Add triples to a named graph::

    curl -X POST -H "Authorization: Bearer <JWT>" -H "Content-Type: application/json" \
      -d '{"triples": [["http://example.org/s", "http://example.org/p", "o"]]}' \
      http://localhost:8000/graphs/http://example.org/graph1/add
    # Response: { "msg": "Triples added to named graph http://example.org/graph1." }

4. Query a named graph::

    curl -X POST -H "Authorization: Bearer <JWT>" -H "Content-Type: application/json" \
      -d '{"query": "?s ?p ?o"}' http://localhost:8000/graphs/http://example.org/graph1/query
    # Response: { "results": [...] }

See the OpenAPI docs for details and adapter support. 

.. _public_sparql_endpoint:

Public SPARQL Endpoint
=====================

AxiusMEM™ provides a public ``GET /sparql`` endpoint for running SPARQL SELECT and ASK queries via HTTP GET.

Endpoint
--------
- ``GET /sparql?query=...`` — run a SPARQL SELECT or ASK query (no authentication required)

Example Usage
-------------

1. Run a SELECT query::

    curl "http://localhost:8000/sparql?query=SELECT%20*%20WHERE%20%7B%20?s%20?p%20?o%20%7D%20LIMIT%2010"
    # Response: { "results": [...] }

2. Run an ASK query::

    curl "http://localhost:8000/sparql?query=ASK%20%7B%20?s%20?p%20?o%20%7D"
    # Response: { "results": [...] }

**Note:** Only read-only queries (SELECT, ASK) are supported. For updates, use the admin API.

See the OpenAPI docs for details and adapter support. 

.. _retry_policy:

Automatic Retry Policy
=====================

AxiusMEM™ automatically retries triplestore and network operations to improve reliability in the face of transient errors.

- **What is retried:**
  - All network/triplestore operations (SPARQL queries, updates, transactions, named graph ops) in supported adapters (GraphDB, Jena, etc.)
  - Retries are triggered on network errors and HTTP 5xx errors
- **Retry strategy:**
  - Up to 3 attempts
  - Exponential backoff (starts at 0.5s, up to 8s)
  - All retries and errors are logged
- **User impact:**
  - Most transient network issues are handled automatically
  - If all retries fail, a clear error is returned to the API/user

**Note:** For persistent errors (e.g., authentication failure, invalid query), no retry is performed.

See the OpenAPI docs and logs for details. 

.. _error_handling:

Error Handling and Retry Responses
=================================

AxiusMEM™ provides clear, user-facing error messages for all API endpoints. If an operation is retried and still fails, the API returns a 503 with a message indicating the retry attempts. For other errors, a 500 is returned with context.

Example Error Responses
----------------------

- **Transient error with retries (503):**

  .. code-block:: json

     {
       "detail": "SPARQL query failed after multiple retries due to a transient error: HTTPConnectionPool(host='localhost', port=3030): Max retries exceeded. Please try again later."
     }

- **Generic server error (500):**

  .. code-block:: json

     {
       "detail": "Add triples to named graph failed: Invalid triple format."
     }

**Note:** For persistent errors (e.g., invalid query, authentication failure), a 400 or 401/403 is returned as appropriate.

See the OpenAPI docs for details and troubleshooting. 

.. _health_metrics_tasks:

Health Check, Metrics, and Tasks Endpoints
=========================================

AxiusMEM™ provides endpoints for health checks, server metrics, and background tasks.

Endpoints
---------
- ``GET /health`` (public): Returns API status and triplestore connectivity
- ``GET /metrics`` (admin-only): Returns server stats (uptime, request count, error count, etc.)
- ``GET /tasks`` (admin-only): Returns a list of background/async tasks (stub for now)

Example Usage
-------------

1. Health check::

    curl http://localhost:8000/health
    # Response: { "status": "ok", "triplestore": "ok" }

2. Metrics (admin)::

    curl -H "Authorization: Bearer <JWT>" http://localhost:8000/metrics
    # Response: { "uptime_seconds": 123, "total_requests": 42, ... }

3. Tasks (admin)::

    curl -H "Authorization: Bearer <JWT>" http://localhost:8000/tasks
    # Response: { "tasks": [] }

See the OpenAPI docs for details and future task support. 

Loading the Default Ontology
---------------------------

AxiusMEM™ distributes its ontology with the library. To load it into your triplestore, simply call:

.. code-block:: python

   from axiusmem import load_default_ontology
   from axiusmem.adapters.base import get_triplestore_adapter_from_env

   adapter = get_triplestore_adapter_from_env()
   load_default_ontology(adapter)
   print("Loaded the default AxiusMEM™ ontology into the triplestore.")

You do not need to specify the ontology file path—AxiusMEM™ will find it automatically. 