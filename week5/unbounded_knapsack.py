def knapsack(items, w):
    V = [0 for x in range(w+1)]
    for (i, _) in enumerate(V):
        for (j, _) in enumerate(items):
            if items[j][0] <= i:
                V[i] = max(V[i], V[i-items[j][0]] + items[j][1])
        
    return V

# (weight, value)
items_arr = ((1, 10), (3, 40), (4, 50), (5, 70))

print(knapsack(items_arr, 8))

