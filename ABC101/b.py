N = input()
int_N = int(N)

S_N = 0
for c in N:
    S_N += int(c)

if int_N % S_N == 0:
    print('Yes')
else:
    print('No')