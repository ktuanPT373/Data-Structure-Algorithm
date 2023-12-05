arr = [23,78,45,8,32,56]
m = len(arr)
while m > 1:
    for i in range(1,m):
        if arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
    m-=1
print(arr)

# Time: O(n^2)
# Space: O(n) 