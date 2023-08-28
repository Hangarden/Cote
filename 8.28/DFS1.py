# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True #방문처리하여 다시 방문하지 않도록
    print(v, end=' ')
    for i in graph[v]: # 인접한 노드를 하나씩 넣어 탐색한다. 보통 아래처럼 되어있지만 안될 경우 sort를 써야 하나?
        if not visited[i]: # 방문처리된 True일 경우에는 False가 되어 실행되지 않는다.
            dfs(graph, i, visited)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

print(dfs(graph, 1, visited))