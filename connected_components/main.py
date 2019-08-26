import collections
import numpy
import pandas
import random
import string


def dfs(index, component, visited, graph):
    """
    Given a vertex, visit all of the adjacent vertices.
    """
    visited[index] = True
    component.append(index)
    connections = graph[index]
    for index in connections:
        if visited[index] is False:
            component = dfs(index, component, visited, graph)
    return component


def connected_components(graph):
    """
    For each vertex, do a DFS to discover all connected vertices.

    Parameters
    ----------
    graph : list-of-lists
    """
    visited = {k: False for k in graph}
    components = []
    for k in graph:
        if visited[k] is False:
            component = dfs(k, [], visited, graph)
            components.append(component)
    return components


def build_graph(edges):
    """
    Parameters
    ----------
    edges : 2-column pandas.DataFrame
    """
    edges = list(edges.itertuples(index=False, name=None))
    graph = collections.defaultdict(lambda: set())
    for e in edges:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def generate_random_time_series(ts_name, mu, sigma):
    ts = numpy.random.normal(mu, sigma, 100)
    ts = pandas.Series(ts, name='ts_value')
    ts = ts.reset_index().assign(ts_name=ts_name)
    return ts


def generate_ts_df():
    """
    Returns
    -------
    ts_df : pandas.DataFrame
        (100 rows, 52 columns)
    """
    ts_df = []
    main_ts = generate_random_time_series('A', 100, 1)
    for ts_name in string.ascii_letters:
        ts = generate_random_time_series(ts_name, 0, random.random()*10)
        ts['ts_value'] = main_ts['ts_value'] + ts['ts_value']
        ts_df.append(ts)
    ts_df = pandas.concat(ts_df)
    ts_df = ts_df.pivot('index', 'ts_name', 'ts_value')
    return ts_df


if __name__ == '__main__':
    ts_df = generate_ts_df()
    corr = ts_df.corr()

    clusters = corr.stack().rename('corr').to_frame()
    clusters.index.names = ['ts1', 'ts2']
    clusters = clusters.reset_index()
    clusters = clusters[lambda row: row['corr'].abs().between(0.6, 0.99)]
    edges = clusters[['ts1', 'ts2']]

    graph = build_graph(edges)
    components = connected_components(graph)
    print(clusters)
    print(components)
