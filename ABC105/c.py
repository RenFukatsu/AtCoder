import math
 
N = int(input())
 
def calc_power(num):
    if num > 1:
        m = 5
        power = 2
        while True:
            if num <= m:
                return_num = power
                break
            else:
                m = m * 4 + 1
                power += 2 
    elif num == 1:
        return_num = 0
    elif num == 0:
        print('0')
        exit()
    else:
        m = -2
        power = 1
        while True:
            if num >= m:
                return_num = power
                break
            else:
                m = m * 4 - 2
                power += 2
 
    return return_num
 
num = N
pre_power = calc_power(N) + 1
ans = ''
while num != 0:
    power = calc_power(num)
    num -= (-2) ** power
    if power == pre_power - 1:
        ans += '1'
    else:
        for _ in range(pre_power - 1 - power):
            ans += '0'
        ans += '1'
    if num == 0:
        for _ in range(power):
            ans += '0'
    pre_power = power
 
print(ans)