from collections import deque

# queue = deque([1])
# print(deque)
# v = queue.popleft()
# print(v)

def BFS(graph, start, visited):
    queue = deque([start]) #queue = deque([1])
    visited[start] = True # visited[1] = True
    while queue:
        v = queue.popleft() # v= 1  # v=2,3,8 # 3,8,7
        print(v, end = '') # print 1 2
        for i in graph[v]: # for i in [2,3,8] # [1,7]
            if not visited[i]: #[1] -> False [7] -> True
                queue.append(i) #queue.append[2], queue.append[3],queue.append[8] append[7]
                visited[i] = True # [2]. [3], [8] visited # [7]visited

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

print(BFS(graph, 1, visited))