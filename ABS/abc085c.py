N, Y = map(int, input().split())

n10 = 0
min_diff = Y - 1000 * N

while True:
    diff = min_diff - 9000 * n10
    if diff < 0:
        break
    n5, mod = divmod(diff, 4000)
    if mod == 0 and (n10 + n5) <= N:
        n1 = N - n10 - n5
        print(n10, n5, n1)
        exit()
    n10 += 1

print('-1 -1 -1')