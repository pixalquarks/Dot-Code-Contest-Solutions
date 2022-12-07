from collections import deque


def lastMaxStanding(numberOfElement, isConnected):
    # WE ARE CONVERTING THIS EDGE FORM GRAPH TO ADJACENCY MATRIX FORMAT
    mx = max([max(i) for i in isConnected])
    n = mx + 1  # NUMBER OF VERTICES IN THE GRAPH

    graph = [[] for _ in range(n)]
    for i in isConnected:
        graph[i[0]].append(i[1])  # GRAPH In THE ADJACENCY LIST FORMAT

    # USING SIMPLE BFS ALGO TO COUNT GRAPH COMPONENTS
    n = len(graph)
    if not n:
        return -1
    visited = [-1] * n
    count = 0
    for i in range(n):
        if visited[i] == -1:
            count += 1
            q = deque([i])
            while q:
                vertex = q.popleft()
                for j in graph[vertex]:
                    if visited[j] == -1:
                        q.append(j)
                        visited[j] = 0
    res = (
        n / count
    )  # AVERAGE NUMBER OF VERTICES IN EACH COMPONENT, i.e. Average number of villages in a cluster.
    return round(res, 2)
