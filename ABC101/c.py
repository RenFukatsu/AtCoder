N, K = map(int, input().split())
A = list(map(int, input().split()))

div, mod = divmod(N - 1, K - 1)
if mod == 0:
    print(div)
else:
    print(div + 1)
