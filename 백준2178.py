N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input())))
maze_result = [[0]*M for i in range(N)]
maze_result[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(maze, xpos, ypos):
    queue = []
    queue.append([xpos, ypos])
    maze[xpos][ypos]= 0
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(0, 4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if maze[next_x][next_y] == 1:
                    maze[next_x][next_y] = 0
                    queue.append([next_x, next_y])
                    maze_result[next_x][next_y] = maze_result[current_x][current_y]+1
    return maze_result[N-1][M-1]


print(bfs(maze, 0, 0))
