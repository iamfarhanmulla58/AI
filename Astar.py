graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}
h = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}
open_list = [('A', 0)]
cost = {'A': 0}
parent = {'A': None}

while open_list:
    current = min(open_list, key=lambda x: x[1])
    node = current[0]
    open_list.remove(current)
    if node == 'G':
        break
    for neighbour, edge_cost in graph[node]:
        new_cost = cost[node] + edge_cost
        if neighbour not in cost or new_cost < cost[neighbour]:
            cost[neighbour] = new_cost
            f = new_cost + h[neighbour]
            open_list.append((neighbour, f))
            parent[neighbour] = node
path = []
node = 'G'
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()
print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost['G'])