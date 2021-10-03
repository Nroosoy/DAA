def calc_degrees(G):
    D = {}
    for i in range(len(G)):
        D[i] = 0
        
    for v in G:
        for e in v:
            D[e] += 1

    return D

def init_S(D):
    S = []
    for i in D:
        if D[i] == 0:
            S.append(i)
    return S

def topological_sort(G):
    topo = []
    D = calc_degrees(G)
    S = init_S(D)
    while len(S) > 0:
        curr = S.pop(0)
        topo.append(curr)
        for out in G[curr]:
            D[out] -= 1
            if D[out] == 0:
                S.append(out)
    return topo


# Graph from the lecture slides
G = [
    [3, 4, 5],
    [5, 4],
    [4, 8],
    [7],
    [6],
    [7],
    [8, 7],
    [],
    []
]

print(topological_sort(G))