N = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(N):
    while not a[i]%2:
        a[i] = a[i] // 2
        count += 1

print(count)
