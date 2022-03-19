from collections import deque
import sys


input = sys.stdin.readline
N, K = map(int, input().split())
result_count = 0
visit_count = 0
visited = [[result_count, visit_count] for _ in range(100001)]

def bfs(subin):
    queue = deque([subin])
    visited[subin][0] = 0
    visited[subin][1] = 1
    while queue:
        current_subin = queue.popleft()
        for i in [current_subin*2, current_subin-1, current_subin+1]:
            if 0<=i<=100000:
                if visited[i][0] == 0:
                    visited[i][0] = visited[current_subin][0] + 1
                    visited[i][1] = 1
                    queue.append(i)
                else:
                    if visited[i][0] == visited[current_subin][0]+1:
                        visited[i][1] += 1

bfs(N)
print(visited[K][0])
print(visited[K][1])