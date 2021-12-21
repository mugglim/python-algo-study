DIV_NUMBER= 1000000007

n = int(input())
dp = [0] * (50 + 1)
dp[0], dp[1], dp[2] = 1, 1, 3

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] + 1

print(dp[n] % DIV_NUMBER)