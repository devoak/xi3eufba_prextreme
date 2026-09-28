import sys

def calculation():
    input = sys.stdin.read().split()
    
    if not input:
        return
    
    n = int(input[0])
    k = int(input[1])
    a = [int(x) for x in input [2:2+n]]
    cont = 0
    
    for i in range(n):
        anomaly = True
        
        for j in range(n):
            if i != j:
                dif = abs(a[i] - a[j])
                if dif <= k:
                    anomaly = False
                    break
                
        if anomaly:
            cont +=1
    print(cont)
    
if __name__ == "__main__":
    calculation()