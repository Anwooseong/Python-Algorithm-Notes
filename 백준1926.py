def bfs(xpos, ypos):
    count = 1
    queue = []
    queue.append([xpos, ypos])
    picture[xpos][ypos] = 0
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if picture[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                    queue.append([next_x, next_y])
                    picture[next_x][next_y] = 0
                    visited[next_x][next_y] = 1
                    count += 1
    return count


n, m = map(int, input().split())
picture = []
cnt, max_value = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    picture.append(list(map(int, input().split())))
visited = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            max_value = max(max_value, bfs(i, j))
print(cnt)
print(max_value)
