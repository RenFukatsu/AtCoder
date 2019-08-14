import heapq

N, M = map(int, input().split())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

score = [] 
scores = []
for i in range(-1, 2, 2):
    for j in range(-1, 2, 2):
        for k in range(-1, 2, 2):
            for info in data:
                heapq.heappush(score, -(i*info[0] + j*info[1] + k*info[2]))
            scores.append(-sum([heapq.heappop(score) for _ in range(M)]))
            score.clear()

print(max(scores))

                