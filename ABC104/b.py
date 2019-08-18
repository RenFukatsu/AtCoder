S = input()

if S[0] == 'A':
    index = S.find('C')
    new_S = S[1:index] + S[(index + 1):]
    if 1 < index < len(S) - 1 and new_S.islower():
        print('AC')
        exit()

print('WA')