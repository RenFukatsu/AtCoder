S = input()

num = 0
for c in S:
    if c == '+':
        num += 1
    elif c == '-':
        num -= 1
print(num)