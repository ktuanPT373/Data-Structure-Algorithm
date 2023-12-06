# a1 = [3,7,2,5,1,4,9]
# a2 = [4,3,2,3,6,1,5,4,9,7]
# n1,n2 = len(a1),len(a2)
n1,n2 = map(int,input().split())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
for i in range(n1-1,-1,-1):
    for j in range(n2-1,-1,-1):
        if a1[i] == a2[j]:
            dp[i][j] = 1 + dp[i+1][j+1]
        else:
            dp[i][j] = max(dp[i][j+1],dp[i+1][j])
print(dp[0][0])