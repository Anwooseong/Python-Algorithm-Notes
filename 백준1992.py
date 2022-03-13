import sys


input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip()))for _ in range(N)]
ans = list()
def recursion(xpos, ypos, n):
    start = arr[xpos][ypos]
    for i in range(xpos, xpos+n):
        for j in range(ypos, ypos+n):
            if start != arr[i][j]:
                n = n//2
                ans.append('(')
                recursion(xpos, ypos, n)
                recursion(xpos, ypos+n, n)
                recursion(xpos+n, ypos, n)
                recursion(xpos+n, ypos+n, n)
                ans.append(')')
                return
    if start == 0:
        ans.append(0)
    else:
        ans.append(1)
recursion(0,0,N)
for value in ans:
    print(value, end='')