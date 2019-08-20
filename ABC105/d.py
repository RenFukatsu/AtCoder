N, M = map(int, input().split())
A = list(map(int, input().split()))
 
mod_dict = dict()
S_mod = [0]
s = 0
for a in A:
    s += a
    mod = s % M
    S_mod.append(mod)
    if not mod in mod_dict.keys():
        mod_dict[mod] = 1
    else:
        mod_dict[mod] += 1
 
if 0 in mod_dict.keys():
    count = mod_dict[0]
else:
    count = 0
for key in mod_dict.keys():
    count += (mod_dict[key] - 1) * mod_dict[key] / 2
 
print(int(count))