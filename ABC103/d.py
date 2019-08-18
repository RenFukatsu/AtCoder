N, M = map(int, input().split())
AB = list(list(map(int, input().split())) for _ in range(M))

AB_sorted = sorted(AB, key=lambda x : x[1])

removed_bridge = []
for ab in AB_sorted:
    if removed_bridge:
        if ab[0] < removed_bridge[-1] < ab[1]:
            continue
    removed_bridge.append(ab[1] - 0.5)

print(len(removed_bridge))