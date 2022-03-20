import sys


input = sys.stdin.readline
N = int(input())

blank = N-1
for i in range(0, N):
    arr = ' '*blank+'*'*(2*i+1)
    print(arr)
    blank -= 1