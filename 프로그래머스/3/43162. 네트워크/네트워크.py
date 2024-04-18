from collections import deque

def solution(n, computers):
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for i in range(n):
                if graph[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer += 1
    
    return answer