import numpy as np
n = int(input())
map = []
for _ in range(n):
    map.append(list(map(int,input().split())))
# n = 12
# map = [[0, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46],
#     [82, 0, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54],
#     [93, 83, 0, 17, 19, 96, 48, 27, 72, 39, 70, 13],
#     [68, 100, 36, 0, 4, 12, 23, 34, 74, 65, 42, 12],
#     [54, 69, 48, 45, 0, 58, 38, 60, 24, 42, 30, 79],
#     [17, 36, 91, 43, 89, 0, 41, 43, 65, 49, 47, 6],
#     [91, 30, 71, 51, 7, 2, 0, 49, 30, 24, 85, 55],
#     [57, 41, 67, 77, 32, 9, 45, 0, 27, 24, 38, 39],
#     [19, 83, 30, 42, 34, 16, 40, 59, 0, 31, 78, 7],
#     [74, 87, 22, 46, 25, 73, 71, 30, 78, 0, 98, 13],
#     [87, 91, 62, 37, 56, 68, 56, 75, 32, 53, 0, 51],
#     [42, 25, 67, 31, 8, 92, 8, 38, 58, 88, 54, 0]]
flat_array = np.array(map).flatten()
unique_sorted_array = np.sort(np.unique(flat_array))
cmin =  unique_sorted_array[1]

visited = {0}
res = 999
config = [0]+[-1]*(n-1)
def calculate(config):
    result = 0
    for i in range(1,len(config)):
        if config[i] == -1:
            return result
        result += map[config[i-1]][config[i]]
    return result + map[config[-1]][0]
def Try(i):
    for v in range(1,n):
        if v not in visited:
            config[i] = v
            visited.add(v)
            if -1 not in config:
                global res
                res = min(res, calculate(config))
            else:
                if calculate(config) + cmin*(n-i) < res:
                    Try(i+1)
            config[i] = -1
            visited.remove(v)
Try(1)
print(res)
