N = int(input())
A = list(map(int, input().split()))

a_sum = 0
for a in A:
    a_sum += 1 / a

print(1/a_sum)
