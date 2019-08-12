n = int(input())
nums = list(map(int, input().split()))
 
nums.sort(reverse=True)
 
Alice_point = 0
Bob_point = 0
 
for i in range(n):
    if i%2 == 0:
        Alice_point += nums[i]
    else:
        Bob_point += nums[i]
 
print(Alice_point - Bob_point)