import sys
from bisect import bisect_right

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    X = int(input_data[1])
    K = int(input_data[2])

    left_cities = []
    right_cities = []

    ptr = 3
    for _ in range(N):
        x = int(input_data[ptr])
        w = int(input_data[ptr+1])
        ptr += 2
        
        if x < X:
            left_cities.append((X - x, w))
        elif x > X:
            right_cities.append((x - X, w))

    left_cities.sort(key=lambda item: item[0])
    right_cities.sort(key=lambda item: item[0])

    L = [0]
    PL = [0]
    current_w = 0
    for dist, w in left_cities:
        L.append(dist)
        current_w += w
        PL.append(current_w)

    R = [0]
    PR = [0]
    current_w = 0
    for dist, w in right_cities:
        R.append(dist)
        current_w += w
        PR.append(current_w)

    max_money = 0

    for i in range(len(L)):
        DL = L[i]
        
        if DL > K:
            break
        
        rem1 = K - 2 * DL
        rem2 = (K - DL) // 2 
        
        DR_max = max(rem1, rem2)

        if DR_max >= 0:
            j = bisect_right(R, DR_max) - 1
            
            if j >= 0:
                total_money = PL[i] + PR[j]
                if total_money > max_money:
                    max_money = total_money

    print(max_money)

if __name__ == '__main__':
    solve()