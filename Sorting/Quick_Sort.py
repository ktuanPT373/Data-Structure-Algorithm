arr = [23,78,45,8,32,56]
def quickSort(arr):
    if len(arr) < 2:
        return arr 
    pivot = arr[0]
    less = [arr[i] for i in range(1,len(arr)) if arr[i] < pivot]
    greater = [arr[i] for i in range(1,len(arr)) if arr[i] >= pivot]
    return quickSort(less) + [arr[0]] + quickSort(greater)
print(quickSort(arr))

# Time : O(nlogn)
# Space : O(n)