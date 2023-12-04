# a, b = map(int, input().split())
# mod = 10**9 + 7

# result = 1
# for _ in range(b):
#     result = (result * a) % mod

# print(result)
x,n = map(int,input().split())
if n < 0:
    x = 1 / x
    n = -n
pow = 1
while n:
    if n & 1:
        pow *= x
    x *= x
    n >>= 1
print(pow%(10**9+7))
