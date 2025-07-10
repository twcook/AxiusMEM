Quick Start
==========

Install AxiusMEM:

.. code-block:: bash

    pip install axiusmem

Or with conda:

.. code-block:: bash

    conda install -c conda-forge axiusmem

Minimal Example:

.. code-block:: python

    from axiusmem import AxiusMEM

    mem = AxiusMEM()
    mem.load_ontology('docs/axiusmem_ontology.ttl')
    mem.connect_graphdb()
    # Add triples, query, manage agent memory, etc.

See the :doc:`api` for full API reference, and :doc:`axiusmem_ontology <axiusmem_ontology.ttl>` for the ontology. 