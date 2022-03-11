import sys


input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split()))for _ in range(N)]
ans = {0:0, 1:0}
def recursion(xpos, ypos, n):
    first = graph[xpos][ypos]
    for i in range(xpos, xpos+n):
        for j in range(ypos, ypos+n):
            if first != graph[i][j]:
                recursion(xpos, ypos, n//2)
                recursion(xpos, ypos+n//2, n//2)
                recursion(xpos+n//2, ypos, n//2)
                recursion(xpos+n//2, ypos+n//2, n//2)
                return
    if first == 0:
        ans[0] = ans[0]+1
    else:
        ans[1] = ans[1]+1
recursion(0,0,N)
print(ans[0])
print(ans[1])