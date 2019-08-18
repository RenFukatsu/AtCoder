N  = int(input())
vs = list(map(float, input().split()))

vs_sorted = sorted(vs)

pre_v = 0.0
for i, v in enumerate(vs_sorted):
    if i == 0:
        pre_v = v
        continue
    pre_v = (pre_v + v) / 2

print(pre_v)