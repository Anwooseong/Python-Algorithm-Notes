import sys


input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split()))for _ in range(N)]
ans = {-1:0, 0:0, 1:0}
def recursion(xpos, ypos, n):
    start = paper[xpos][ypos]
    for i in range(xpos, xpos+n):
        for j in range(ypos, ypos+n):
            if start != paper[i][j]:
                n = n//3
                recursion(xpos, ypos, n)
                recursion(xpos, ypos+n, n)
                recursion(xpos, ypos+2*n,n)
                recursion(xpos+n, ypos, n)
                recursion(xpos+n, ypos+n, n)
                recursion(xpos+n, ypos+2*n, n)
                recursion(xpos+2*n, ypos, n)
                recursion(xpos+2*n, ypos+n, n)
                recursion(xpos+2*n, ypos+2*n, n)
                return
    if start == -1:
        ans[-1] += 1
    elif start == 0:
        ans[0] += 1
    else:
        ans[1] += 1
recursion(0,0,N)
print(ans[-1])
print(ans[0])
print(ans[1])