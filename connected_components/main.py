"""
TODO:
print(M) -> prettyprint
"""
import collections
import itertools
import numpy


def dfs(key1, component, visited, graph):
    """
    Given a vertex, visit all of the adjacent vertices.
    """
    visited[key1] = True
    component.append(key1)
    connections = graph[key1]
    for key2 in connections:
        if visited[key2] is False:
            component = dfs(key2, component, visited, graph)
    return component


def connected_components(graph):
    """
    For each vertex, do a DFS to discover all connected vertices.

    Parameters
    ----------
    graph : Dict[T: Set[T]]

    Returns
    -------
    components : List[List[T]]
        Each element is a component (list of vertices that are directly &
        indirectly connected).
    """
    visited = {k: False for k in graph}
    components = []
    for k in graph:
        if visited[k] is False:
            component = []
            component = dfs(k, component, visited, graph)
            components.append(component)
    return components


def build_graph(edges):
    """
    Parameters
    ----------
    edges : List[Tuple[T, T]]

    Returns
    -------
    graph : Dict[T: Set[T]]
    """
    graph = collections.defaultdict(lambda: set())
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
    return graph


def M_to_edges(M):
    """
    Parameters
    ----------
    M : NxN List[List[int]]
        1 means connection.
        0 means no connection.

    Returns
    -------
    edges : List[Tuple[T, T]]
    """
    edges = []
    for i, row in enumerate(M):
        for j, val in enumerate(row):
            if val == 1:
                edges.append((i, j))
                edges.append((j, i))
    return edges


def build_random_M(N, K):
    """
    Parameters
    ----------
    N : int
        Return an N-by-N.
    K : int
        The number of nodes to connect.

    Returns
    -------
    M : List[List[int]]
        N-by-N list-of-lists.
    """
    combinations = itertools.combinations(range(N), 2)
    combinations = list(combinations)
    edges_indexes = numpy.random.choice(len(combinations), K, replace=False)
    edges = [x for i, x in enumerate(combinations) if i in edges_indexes]

    M = []
    for i in range(N):
        row = [0] * N
        M.append(row)

    for i, j in edges:
        M[i][j] = 1
        M[j][i] = 1
    return M


if __name__ == '__main__':
    test_cases = [
        (
            [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]],
            2
        ),
        (
            [[1, 1, 0],
             [1, 1, 1],
             [0, 1, 1]],
            1
        )
    ]

    for M, expected in test_cases:
        edges = M_to_edges(M)
        graph = build_graph(edges)
        components = connected_components(graph)
        # print(graph)
        # print(components)
        assert len(components) == expected

    N = 10
    M = build_random_M(N, 3)
    edges = M_to_edges(M)
    graph = build_graph(edges)
    components = connected_components(graph)
    for row in M:
        print(row)
    print(components)
