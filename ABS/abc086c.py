N = int(input())

travel_plans = []
for _ in range(N):
    t, x, y = map(int, input().split())
    travel_plans.append([t, x, y])

current = [0, 0, 0]
for plan in travel_plans:
    diff_t = plan[0] - current[0]
    diff_x = plan[1] - current[1]
    diff_y = plan[2] - current[2]
    if diff_t >= diff_x + diff_y and (diff_t - diff_x - diff_y) % 2 == 0:
        current = plan
    else:
        print('No')
        exit()

print('Yes')