#PYTHON 
n = int(input())
paths = []
for _ in range(n):
    paths.append(list(map(int,input().split())))
paths.sort(key=lambda x:x[1])
route = []
route.append(paths[0])
for i,j in paths:
  if i > route[-1][1]:
    route.append([i,j])
print(len(route))
