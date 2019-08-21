N, M, Q = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
pq = [list(map(int, input().split())) for _ in range(Q)]

XY = [[0 for _ in range(N)] for _ in range(N)]
for l, r in LR:
    XY[l - 1][r - 1] += 1

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            XY[i][j] += XY[i][j - 1]
        elif j == 0:
            XY[i][j] += XY[i - 1][j]
            pre_im1_j = XY[i - 1][j]
        else:
            if XY[i - 1][j] == pre_im1_j:
                XY[i][j] += XY[i][j - 1]
            else:
                XY[i][j] += XY[i][j - 1] + XY[i - 1][j] - pre_im1_j
                pre_im1_j = XY[i - 1][j]

for p, q in pq:
    if p != 1:
        print(XY[q - 1][q - 1] + XY[p - 2][p - 2] - XY[p - 2][q - 1] - XY[q - 1][p - 2])
    else:
        print(XY[q - 1][q - 1])

