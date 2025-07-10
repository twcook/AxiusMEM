import os
import time
import json
from rdflib import Graph, URIRef, Literal, Namespace
from axiusmem.core import AxiusMEM
from axiusmem.graphdb_adapter import GraphDBAdapter

def get_env(var, default=None):
    v = os.getenv(var)
    if not v:
        if default is not None:
            return default
        raise RuntimeError(f"Env var {var} not set.")
    return v

BENCH_NS = Namespace("http://axiusmem.org/bench/")

def benchmark_ingestion(triple_count=10000, batch_size=1000, mode='incremental'):
    """
    Benchmark triple ingestion (incremental or bulk).
    Returns: dict with timing and throughput.
    """
    g = Graph()
    # Generate synthetic triples
    for i in range(triple_count):
        g.add((BENCH_NS[f"s{i}"], BENCH_NS[f"p"], Literal(f"o{i}")))
    adapter = GraphDBAdapter(
        get_env("AGENT_MEMORY_URL"),
        os.getenv("GRAPHDB_USER"),
        os.getenv("GRAPHDB_PASSWORD")
    )
    repo_id = get_env("GRAPHDB_REPO_ID")
    start = time.time()
    if mode == 'bulk':
        tmpfile = "bench_bulk.ttl"
        g.serialize(destination=tmpfile, format="turtle")
        success = adapter.bulk_load(repo_id, tmpfile)
        os.remove(tmpfile)
        assert success
    else:
        triples = list(g)
        for i in range(0, len(triples), batch_size):
            batch = triples[i:i+batch_size]
            for s, p, o in batch:
                update = f"INSERT DATA {{ <{s}> <{p}> \"{o}\" }}"
                adapter.sparql_update(repo_id, update)
    elapsed = time.time() - start
    return {
        'mode': mode,
        'triple_count': triple_count,
        'batch_size': batch_size,
        'elapsed_sec': elapsed,
        'throughput_tps': triple_count / elapsed
    }

def benchmark_query_latency(query_type='point', repetitions=10):
    """
    Benchmark query latency for a given query type.
    Returns: dict with timing stats.
    """
    adapter = GraphDBAdapter(
        get_env("AGENT_MEMORY_URL"),
        os.getenv("GRAPHDB_USER"),
        os.getenv("GRAPHDB_PASSWORD")
    )
    repo_id = get_env("GRAPHDB_REPO_ID")
    if query_type == 'point':
        query = "SELECT * WHERE { ?s ?p ?o } LIMIT 1"
    elif query_type == 'temporal':
        # Example: temporal query (customize as needed)
        query = "SELECT * WHERE { ?s ?p ?o } LIMIT 10"
    elif query_type == 'traversal':
        query = "SELECT * WHERE { ?s ?p1 ?mid . ?mid ?p2 ?o } LIMIT 1"
    else:
        raise ValueError("Unknown query_type")
    times = []
    for _ in range(repetitions):
        start = time.time()
        adapter.sparql_select(repo_id, query)
        times.append(time.time() - start)
    return {
        'query_type': query_type,
        'repetitions': repetitions,
        'min_latency': min(times),
        'max_latency': max(times),
        'avg_latency': sum(times) / len(times)
    }

def benchmark_scalability(sizes=[1000, 10000, 100000]):
    """
    Benchmark ingestion and query performance as graph size increases.
    Returns: list of dicts with results for each size.
    """
    results = []
    for size in sizes:
        ingest = benchmark_ingestion(triple_count=size, batch_size=1000, mode='bulk')
        query = benchmark_query_latency(query_type='point', repetitions=5)
        results.append({'size': size, 'ingestion': ingest, 'query': query})
    return results

def benchmark_resilience():
    """
    Simulate GraphDB outage and test error handling (manual step).
    Returns: dict with result (stub).
    """
    # In practice, this would require stopping GraphDB or blocking network.
    # Here, we just simulate a connection error.
    try:
        adapter = GraphDBAdapter('http://localhost:9999')
        adapter.test_connection()
    except Exception as e:
        return {'resilience': 'handled', 'error': str(e)}
    return {'resilience': 'not tested'}

def report_results(results, format='markdown'):
    """
    Output benchmark results in the specified format.
    """
    if format == 'json':
        print(json.dumps(results, indent=2))
    elif format == 'markdown':
        if isinstance(results, list):
            for r in results:
                print(f"### Size: {r['size']}")
                print(f"- Ingestion: {r['ingestion']}")
                print(f"- Query: {r['query']}")
        else:
            print(f"```")
            print(json.dumps(results, indent=2))
            print(f"```")
    else:
        print(results)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="AxiusMEM Benchmark Suite")
    parser.add_argument('--ingest', action='store_true', help='Run ingestion benchmark')
    parser.add_argument('--query', action='store_true', help='Run query latency benchmark')
    parser.add_argument('--scalability', action='store_true', help='Run scalability benchmark')
    parser.add_argument('--resilience', action='store_true', help='Run resilience benchmark')
    parser.add_argument('--format', default='markdown', help='Output format')
    args = parser.parse_args()
    if args.ingest:
        res = benchmark_ingestion()
        report_results(res, args.format)
    if args.query:
        res = benchmark_query_latency()
        report_results(res, args.format)
    if args.scalability:
        res = benchmark_scalability()
        report_results(res, args.format)
    if args.resilience:
        res = benchmark_resilience()
        report_results(res, args.format)

if __name__ == '__main__':
    main() 