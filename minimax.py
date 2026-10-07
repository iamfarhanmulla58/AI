def minimax(depth, node, maximizing, tree):

    if depth == 2:
        return tree[node]

    values = []

    for child in tree[node]:
        values.append(
            minimax(depth+1, child, not maximizing, tree)
        )

    if maximizing:
        return max(values)
    else:
        return min(values)

tree = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':3,
    'E':5,
    'F':2,
    'G':9
}

print("Minimax Value:",
      minimax(0,'A',True,tree))