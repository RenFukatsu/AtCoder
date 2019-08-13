D, N = map(int, input().split())

if N == 100:
    num = 101 * (100**D)
else:
    num = N * (100**D)

print(num)