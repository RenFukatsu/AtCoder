n = int(input())
nums = list(map(int, input().split()))
 
count = 0
while True:
    for i in range(n):
        num = nums[i]
        if (num%2) == 1:
            print(count)
            exit()
        else:
            nums[i] = num / 2
    count += 1