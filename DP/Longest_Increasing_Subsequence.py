#PYTHON 
import time
n = int(input())
arr = list(map(int,input().split()))
# start = time.time()
# dp = [1]* n
# for i in range(1,n):
#     dp[i] = max([1+dp[j] for j in range(i-1,-1,-1) if arr[j] < arr[i]]+[1])
# print(max(dp))
# end = time.time()
# print('running time:', end-start)
print(len(arr))