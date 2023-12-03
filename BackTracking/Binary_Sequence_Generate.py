#PYTHON 
n = int(input())
arr = [0]*n
def solution():
    print(''.join(str(i) for i in arr))

def backtrack(k):
    for i in range(0,2):
        arr[k] = i
        if k == n-1:
            solution()
        else: 
            backtrack(k+1)

backtrack(0)
