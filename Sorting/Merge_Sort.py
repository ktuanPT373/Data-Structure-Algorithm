arr = [23,78,45,8,32,56]

def mergeSort(arr):
    if len(arr) == 1:
        return arr 
    m = len(arr)//2
    l = arr[:m]
    r = arr[m:]
    mergeSort(l)
    mergeSort(r)
    return merge(l,r)

def merge(a1,a2):
    i,j = 0,0
    res = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i+=1
        else:
            res.append(a2[j])
            j+=1
    if i < len(a1):
        res += a1[i:]
    elif j < len(a2):
        res += a2[j:]
    return res
print(mergeSort(arr))


# Time : O(nlogn)
# Space : O(n)