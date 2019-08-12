n, a, b = map(int, input().split())
 
sum_num = 0
for i in range(1, n+1):
    s = str(i)
    num = 0
    for c in s:
        num += int(c)
    if(a <= num and num <= b):
        sum_num += i
print(sum_num)