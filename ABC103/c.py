from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

lcm = reduce(lambda x, y: (x * y) // gcd(x, y), A)

score = 0
for a in A:
    score += (lcm - 1) % a

print(score)