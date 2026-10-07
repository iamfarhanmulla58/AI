from collections import deque

def water_jug(cap1, cap2, target):

    queue = deque([((0,0), [])])
    visited = {(0,0)}

    while queue:
        (a,b), path = queue.popleft()

        if a == target or b == target:
            return path + [(a,b)]

        states = [
            (cap1,b),
            (a,cap2),
            (0,b),
            (a,0),
            (a-min(a,cap2-b), b+min(a,cap2-b)),
            (a+min(b,cap1-a), b-min(b,cap1-a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path+[(a,b)]))

result = water_jug(4,3,2)

print("Steps:")
for state in result:
    print(state)