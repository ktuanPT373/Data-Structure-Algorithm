#PYTHON 
#PYTHON 
n = int(input())
m = set()
x = [0]*n
def Try(i):
    for v in range(1,n+1):
        if v not in m:
            x[i] = v
            m.add(v)
            if i == n-1:
                print(*x)
            else:
                Try(i+1)
            m.remove(v)
Try(0)
