# a, b = map(int, input().split())
# mod = 10**9 + 7

# result = 1
# for _ in range(b):
#     result = (result * a) % mod

# print(result)
MOD = 10**9 + 7
def power_mod(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        h = power_mod(a,b/2)
        return (h*h) 
    else:
        return (a*power_mod(a,b-1)) 
a, b = map(int, input().split())
result = power_mod(a,b)
print(result%MOD)