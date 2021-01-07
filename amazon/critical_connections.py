"""

Input:
numOfServers an integer representing number of servers in the data center;
numOfConnections an integer representing number of connections between the servers;
connections a list of pairs of integers representing the connections between the two servers.

Output
Return a list of pairs of integers representing the critical connections.
If there are no critical connections, return a list with an empty pair.
"""
import collections


def critical_connections(n, connections):
    def make_graph(connections):
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        return graph

    graph = make_graph(connections)
    connections = [sorted(c) for c in connections]
    connections = [tuple(c) for c in connections]
    connections = set(connections)
    rank = collections.defaultdict(lambda: -2)

    def dfs(node, depth):
        # visited
        if rank[node] >= 0:
            return rank[node]
        rank[node] = depth
        min_back_depth = n
        for neighbor in graph[node]:
            # parent
            if rank[neighbor] == depth - 1:
                continue
            back_depth = dfs(neighbor, depth + 1)
            # visited before / cycle
            if back_depth <= depth:
                connections.remove(tuple(sorted((node, neighbor))))
            min_back_depth = min(min_back_depth, back_depth)
        return min_back_depth

    dfs(list(graph.keys())[0], 0)
    return list(connections)


if __name__ == "__main__":
    assert critical_connections(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]) == [
        (1, 2),
        (4, 5),
    ]
