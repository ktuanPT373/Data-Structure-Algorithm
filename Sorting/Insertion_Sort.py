arr = [23,78,45,8,32,56]
for k in range(1,len(arr)):
    for i in range(k):
        if arr[i] > arr[k]:
            arr[i],arr[k] = arr[k],arr[i]
print(arr)

# Time : O(n^2)
# Space: O(1)