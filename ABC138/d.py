N, Q = map(int, input().split())

Tree = []
for _ in range(1, N):
    a, b = map(int, input().split())
    Tree.append([a, b])

Tree_sorted = sorted(Tree, key=lambda x:x[0])

P = []
X = []
for _ in range(Q):
    p, x = map(int, input().split())
    P.append(p)
    X.append(x)

scores = [0 for _ in range(N + 1)]
for i in range(Q):
    scores[P[i]] += X[i]

for tree in Tree_sorted:
    scores[tree[1]] += scores[tree[0]]

for i, score in enumerate(scores):
    if i == 0:
        continue
    print(score, end=' ')
