import sys


input = sys.stdin.readline

def bfs(xpos, ypos):
    queue = list()
    queue.append([xpos, ypos])
    visited[xpos][ypos] = True
    while queue:
        current_x, current_y = queue.pop(0)
        for i in range(8):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<h and 0<=next_y<w and visited[next_x][next_y] == False and soil_list[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    soil_list = list()
    visited = [[False]*w for _ in range(h)]
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    for _ in range(h):
        soil_list.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if soil_list[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                count += 1
    print(count)