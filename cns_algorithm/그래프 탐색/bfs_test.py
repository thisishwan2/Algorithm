from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start]=1

    while q:
        v=q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1

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

visited=[0]*9

bfs(graph,1,visited)