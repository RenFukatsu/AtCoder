N = int(input())
 
num_set = []
seven_count = 0
 
while seven_count * 7 <= N:
    total = 7 * seven_count
    while total <= N:
        num_set.append(total)
        total += 4
    seven_count += 1
 
num_set = set(num_set)
 
if N in num_set:
    print('Yes')
else:
    print('No')