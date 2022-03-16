import sys


input = sys.stdin.readline
N = int(input())
jump_list = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = jump_list[0]


def result(n):
    if dp[0] == 0:
        return ans
    
ans = 0
        