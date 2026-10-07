from collections import deque
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
} 
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    order=[]
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order
print("BFS Traversal:",bfs(graph,'A'))