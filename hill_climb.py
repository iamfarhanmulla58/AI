def function(x):
    return -(x-3)**2 + 9

def hill_climbing(start):

    x = start

    while True:

        neighbours = [x-1, x+1]

        best = max(neighbours, key=function)

        if function(best) <= function(x):
            return x

        x = best

result = hill_climbing(0)

print("Maximum found at:", result)
print("Maximum value:", function(result))