import sys


input = sys.stdin.readline
N = int(input())
arr = list(int(input()) for _ in range(N))
arr.sort() #sort 시간복잡도는 nlgn
for i in arr:
    print(i)