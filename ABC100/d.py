import heapq
import itertools

N, M = map(int, input().split())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

scores = []
for info in list(itertools.combinations(data, M)):
    print('info', info)
    beuty_score = abs(info[0][0] + info[1][0] + info[2][0])
    taste_score = abs(info[0][1] + info[1][1] + info[2][1])
    popular_score = abs(info[0][2] + info[1][2] + info[2][2])
    print(beuty_score)
    print(taste_score)
    print(popular_score)
    heapq.heappush(scores, -(beuty_score + taste_score + popular_score))


print(-heapq.heappop(scores))

