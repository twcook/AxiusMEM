Agent Memory Utilities
=====================

AxiusMEM™ provides utilities to store, retrieve, and format agent-specific memories and context in the knowledge graph, and to propose ontology updates.

Overview
--------
- Store and retrieve agent memories as RDF nodes.
- Retrieve context for an agent.
- Format context for LLM prompt consumption.
- Propose ontology updates from agents.

Example Usage
-------------

.. code-block:: python

   from rdflib import Graph
   from axiusmem.agent_utils import (
       store_agent_memory, retrieve_agent_memories,
       get_context_for_agent, format_context_for_llm, propose_ontology_update
   )

   g = Graph()
   agent_id = "agent-001"

   # Store a memory
   mem_uri = store_agent_memory(g, agent_id, {"event": "login", "timestamp": "2024-07-01"})

   # Retrieve all memories for an agent
   memories = retrieve_agent_memories(g, agent_id)

   # Get context for an agent
   context = get_context_for_agent(g, agent_id)

   # Format context for LLM prompt
   prompt = format_context_for_llm(context, format="text")

   # Propose an ontology update
   propose_ontology_update(g, agent_id, {"type": "Class", "name": "SmartDevice"})

See the API reference for full method documentation. 