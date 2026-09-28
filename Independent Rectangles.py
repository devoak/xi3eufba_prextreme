def add_tower(w,h, towers):
    ref = list(towers)
    removed = 0
    for i, (tower_w, tower_j) in enumerate(ref):
        if w < tower_w and h < tower_j:
            return
        if w > tower_w and h > tower_j:
            del towers[i-removed]
            removed +=1
    towers.append([w,h])

n = int(input())
towers = []
for _ in range(n):
    w,h = map(int, input().split())
    add_tower(w,h, towers)

print(len(towers))
