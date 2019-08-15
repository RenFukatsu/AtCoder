from statistics import median

N = int(input())
A = list(map(int, input().split()))

A_star = [a - (i + 1) for i, a in enumerate(A)]

def calc_score(b):
    score = 0
    for a in A_star:
        score += abs(a - b)
    return score

print(calc_score(int(median(A_star))))