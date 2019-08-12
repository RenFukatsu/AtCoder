n = int(input())
nums = []
 
for i in range(n):
    nums.append(int(input()))
 
s_nums = set(nums)
 
print(len(s_nums))