from itertools import permutations

cities = ['A','B','C','D']

cost = {
    'A': {'A':0,'B':10,'C':15,'D':20},
    'B': {'A':10,'B':0,'C':35,'D':25},
    'C': {'A':15,'B':35,'C':0,'D':30},
    'D': {'A':20,'B':25,'C':30,'D':0}
}

best_route = None
min_cost = float('inf')

for p in permutations(cities[1:]):
    route = ('A',) + p + ('A',)

    total = 0
    for i in range(len(route)-1):
        total += cost[route[i]][route[i+1]]

    if total < min_cost:
        min_cost = total
        best_route = route

print("Best Route:", " -> ".join(best_route))
print("Minimum Cost:", min_cost)