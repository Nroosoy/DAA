from maximum_sub_array import max_sub

def max_diff(A):
    diffs = []
    for i in range(len(A) - 1):
        diffs.append(A[i+1] - A[i])

    start, end, diff = max_sub(diffs)
    # end is always the second element of a diff pair, hence the end+1
    return [start, end+1, diff]

print(max_diff([1, 2, -3, 4, -6, 7]))