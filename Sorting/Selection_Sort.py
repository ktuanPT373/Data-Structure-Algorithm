arr = [23,78,45,8,32,56]
i = 0
while i < len(arr):
    m = 999
    mem = 0
    for j in range(i,len(arr)):
        if arr[j] < m:
            mem = j
            m = arr[j]
    arr[i],arr[mem] = arr[mem],arr[i]
    i+=1
print(arr)
        
# Time : O(n^2)
# Space : O(1)

