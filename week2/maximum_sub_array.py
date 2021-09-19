def max_sub(A):
    max = -99999 #just something smaller than any value in the arrays
    max_start = 0
    max_end = 0
    curr_start = 0
    max_here = 0
    for (i, v) in enumerate(A):
        max_here += v
        if max < max_here:
            max = max_here
            max_end = i
            max_start = curr_start
        if max_here < 0:
            max_here = 0
            # next maximum segment must start at earliest from the next index
            curr_start = i+1
    return [max_start, max_end, max]

