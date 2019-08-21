S = input()
K = int(input())

pos = 1
for c in S:
    num = int(c)
    if num == 1 and pos < K:
        pos += 1
        continue
    else:
        print(num)
        break