import math

def partition(A, p):
    B, C = [], []
    for a in A:
        if a < p:
            B.append(a)
        elif a > p:
            C.append(a)
    B.append(p)
    return (B, C)

def select(A, j):
    if len(A) // 5 == 0:
        return sorted(A)[j]
    
    chunks = [sorted(A[x:x+5]) for x in range(0, len(A), 5)]
    M = [a[len(a)//2] for a in chunks]
    
    p = select(M, (len(A) // 5) // 2)
    B, C = partition(A, p)
    x = len(B)
    
    if j == x:
        return p
    elif x > j:
        return select(B, j)
    return select(C, j-x)
   

for i in range(2, 200):
    lin_a = [x for x in range(1, i)]
    
    print(lin_a[len(lin_a) // 2], end=", ")
    test = select(lin_a, len(lin_a) // 2)
    print(test)