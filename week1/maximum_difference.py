def find_min(A, i, j):
    min_idx = i
    for idx in range(i, j):
        if A[idx] < A[min_idx]:
            min_idx = idx
    return min_idx

def find_max(A, i, j):
    max_idx = i
    for idx in range(i, j):
        if A[idx] > A[max_idx]:
            max_idx = idx
    return max_idx

def max_diff(A, i, j):
    if j-i <= 1:
        return [i, j]
    halfway = (i + j) // 2
    
    own_min = find_min(A, i, halfway)
    own_max = find_max(A, halfway, j)
    
    left_min, left_max = max_diff(A, i, halfway)
    right_min, right_max = max_diff(A, halfway, j)
    
    own_diff = A[own_max] - A[own_min]
    left_diff = A[left_max] - A[left_min]
    right_diff = A[right_max] - A[right_min]
    
    largest_diff = max(own_diff, left_diff, right_diff)

    if largest_diff == own_diff:
        return [own_min, own_max]
    if largest_diff == right_diff:
        return [right_min, right_max]
    return [left_min, left_max]

arr = [110, 1, 3, 2, 13, -1, 11, 5]
low, high = max_diff(arr, 0, len(arr)-1)
print("Optimal time to buy is at", low, "with value", arr[low], "and to sell at", high, "with value", arr[high], "for gains of", arr[high] - arr[low])
