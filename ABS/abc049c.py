S = input()
T = ''

point = 0

while T != S:
    if S[point:point+11] == 'dreameraser':
        T += 'dreameraser'
        point += 11
    elif S[point:point+10] == 'dreamerase':
        T += 'dreamerase'
        point += 10
    elif S[point:point+7] == 'dreamer':
        T += 'dreamer'
        point += 7
    elif S[point:point+5] == 'dream':
        T += 'dream'
        point += 5
    elif S[point:point+6] == 'eraser':
        T += 'eraser'
        point += 6
    elif S[point:point+5] == 'erase':
        T += 'erase'
        point += 5
    else:
        print('NO')
        exit()

print('YES')