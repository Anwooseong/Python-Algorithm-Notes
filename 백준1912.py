import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
dp = []
def result(n):
    if n==N:
        return
    else:
        if n == 0:
            dp.append(num_list[0])
        else:
            dp.append(max(dp[n-1]+num_list[n], num_list[n]))
        result(n+1)
    
result(0)
print(max(dp))