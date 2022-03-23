import sys


input = sys.stdin.readline
ans_dict = {'W':0, 'B':0}
N, M = map(int, input().split())
graph = list(list(map(str, input().rstrip())) for _ in range(M))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(xpos, ypos):
    count = 1
    queue = list()
    queue.append([xpos, ypos])
    point = graph[xpos][ypos]
    graph[xpos][ypos] = 'C'
    while queue:
        current_x, current_y = queue.pop(0)
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<M and 0<=next_y<N and graph[next_x][next_y] == point:
                graph[next_x][next_y] = 'C'
                queue.append([next_x, next_y])
                count += 1
    return count*count
            

for i in range(M): #세로
    for j in range(N): #가로
        if graph[i][j] == 'W':
            ans_dict['W'] += bfs(i,j)
        if graph[i][j] == 'B':
            ans_dict['B'] += bfs(i,j)
print(ans_dict['W'], end=' ')
print(ans_dict['B'])