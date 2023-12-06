arr = [23,78,45,8,32,56]
arr = [3,5,4,6,8,7,9,1,2]
N = len(arr)
def heapify(arr,i,N):
    l = 2*i
    r = 2*i + 1
    m = i
    if l < N and arr[l] > arr[i]:
        m = l
    if r < N and arr[r] > arr[m]:
        m = r
    if m != i:
        arr[i],arr[m] = arr[m],arr[i]
        heapify(arr,m,N)
def build_heap(arr):
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i,N)          
def heap_sort(arr,N):
    build_heap(arr)
    for i in range(N-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i-1)

heap_sort(arr,N)
print(arr)