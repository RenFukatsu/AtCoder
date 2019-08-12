num_500yen = int(input())
num_100yen = int(input())
num_50yen = int(input())
total_fee = int(input())
 
count = 0
for i in range(num_500yen+1):
    for j in range(num_100yen+1):
        for k in range(num_50yen+1):
            total = 500*i + 100*j + 50*k
            if(total == total_fee):
                count += 1
print(count)