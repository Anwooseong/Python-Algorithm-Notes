#1 -> 1
#2 -> 3
#3 -> 5
#4 -> 11
#dp[n] = dp[n-1] + dp[n-2]

n = int(input())
dp = [0 for _ in range(n + 1)]
for i in range(n + 1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 3
    else:
        dp[i] = dp[i-1] + 2*dp[i-2]
        
print(dp[n]%10007)