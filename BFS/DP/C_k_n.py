#PYTHON 
k,n = list(map(int,input().split()))
dp = [[0]*(n+1) for _ in range(k+1)]
for i in range(k+1):
    for j in range(n+1):
        if i == 0 or i == j:
            dp[i][j] = 1
        elif j < i:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
print(dp[k][n]%(10**9+7))
