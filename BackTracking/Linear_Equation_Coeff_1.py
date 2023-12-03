#PYTHON 
#PYTHON 
k,n = map(int,input().split())
res = [0]*k
def backtrack(i,n):
    for v in range(1,n+1):
        res[i] = v
        if i == k-1:
            res[i] = n
            print(*res)
            break
        else:
            backtrack(i+1,n-v)
        res[i] = 0
backtrack(0,n)
