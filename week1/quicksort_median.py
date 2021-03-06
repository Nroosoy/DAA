from linear_median import select

def partition(A, p):
    B, C = [], []
    for x in A:
        if x < p:
            B.append(x)
        else:
            C.append(x)

    return (B, C)

def quicksort(A):
    if len(A) <= 1:
        return A
    p = select(A, len(A) // 2)
    
    B, C = partition(A, p)
    left = quicksort(B)
    right = quicksort(C)
    return left + right

if __name__ == '__main__':
    quicksort([x for x in range(100_000, 1, -1)])