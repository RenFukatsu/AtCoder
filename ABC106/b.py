N = int(input())

def find_divisor_num(n):
    count = 0
    i = 1
    while i**2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if n == i**2:
        count += 1
    return count

count = 0
for i in range(1, N+1, 2):
    divisor_num = find_divisor_num(i)
    if divisor_num == 8:
        count += 1

print(count)