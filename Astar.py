from heapq import heappush, heappop
class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows else 0
        self.start = start
        self.goal = goal

    def heuristic(self, cell):
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])

    def neighbors(self, cell):
        r, c = cell
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != 1:
                yield (nr, nc)

    def find_path(self):
        open_heap = []
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}

        heappush(open_heap, (f_score[self.start], self.start))

        while open_heap:
            _, current = heappop(open_heap)

            if current == self.goal:
                return self._reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor)
                    heappush(open_heap, (f_score[neighbor], neighbor))

        return None

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


def print_grid(grid, path=None):
    path_set = set(path) if path else set()
    for r, row in enumerate(grid):
        line = []
        for c, cell in enumerate(row):
            if (r, c) in path_set:
                line.append('P')
            elif cell == 1:
                line.append('#')
            elif (r, c) == start:
                line.append('S')
            elif (r, c) == goal:
                line.append('G')
            else:
                line.append('.')
        print(' '.join(line))


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]
    start = (0, 0)
    goal = (4, 4)

    a_star = AStar(grid, start, goal)
    path = a_star.find_path()

    if path:
        print("Path found:", path)
    else:
        print("No path found.")

    print_grid(grid, path)
