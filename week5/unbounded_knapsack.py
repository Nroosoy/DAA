""""Week 5 exercises regarding knapsack problem"""

import datetime

def knapsack(items, max_weight):
    """
    Classical DP solution to knapsack problem
    items       -- an iterable containing tuples (weight, value)
    max_weight  -- integer indicating the max weight the knapsack can hold
    """
    solutions = [0 for x in range(max_weight+1)]
    for i in range(0, max_weight + 1):
        for (weight, value) in items:
            if weight <= i:
                solutions[i] = max(solutions[i], solutions[i - weight] + value)

    return solutions

def get_solution(solutions, weight):
    """"Gets the solution from the given map"""
    if weight in solutions:
        return solutions[weight]
    return 0

def knapsack_map(items, max_weight):
    """Same as the traditional DP solution but uses a map instead of an array"""
    solutions = {}
    for i in range(0, max_weight + 1):
        for (weight, value) in items:
            if weight <= i:
                solutions[i] = max(
                    get_solution(solutions, weight),
                    get_solution(solutions, i - weight) + value
                )
    return solutions

# (weight, value)
items_arr = ((1, 10), (3, 40), (4, 50), (5, 70))

print(knapsack(items_arr, 8))

