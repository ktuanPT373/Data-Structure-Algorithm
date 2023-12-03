#PYTHON 
n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]*len(arr)
for i in range(1,len(dp)):
  dp[i] = dp[i-1] + arr[i] if dp[i-1] > 0 else arr[i]
print(max(dp))
