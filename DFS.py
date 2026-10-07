from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': []
}
start = 'A'
goal = 'H'
def dfs(graph, start, goal=None):
    visited = set()
    order = []

    def dfs_visit(node):
        if node in visited:
            return goal is not None and node == goal
        visited.add(node)
        order.append(node)
        if goal is not None and node == goal:
            return True
        for neighbor in graph.get(node, []):
            if dfs_visit(neighbor):
                return True
        return False
    found = dfs_visit(start)
    return order, found
print("DFS Traversal:", dfs(graph, start, goal)[0])
