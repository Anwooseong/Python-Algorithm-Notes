import sys


input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
num_list = reversed(num_list)
dp = []
def result(n):
    if n == 0:
        dp.append(num_list[n])
    if n == 1:
        imsi = dp[0]+num_list[1]
        imsi_2 = num_list[1]
        dp.append(max(dp[0], imsi, imsi_2))
print(num_list)
##dp문제인데 그 앞에 있던 것과 비교했을때 현재것이 더 크면 그 값을 가지도록 코딩