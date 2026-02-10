import copy

def heuristic(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_moves(state):
    x, y = find_blank(state)
    moves = []
    directions = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
    for nx, ny in directions:
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def best_first_search(start, goal):
    current = start
    visited = []
    step = 0
    while current != goal:
        print("Step", step)
        for row in current:
            print(row)
        print()
        visited.append(current)
        next_states = generate_moves(current)
        next_states = [s for s in next_states if s not in visited]
        if not next_states:
            print("No solution")
            return
        current = min(next_states, key=lambda x: heuristic(x, goal))
        step += 1
    print("Goal State Reached")
    for row in goal:
        print(row)

print("Enter initial state:")
start = [list(map(int, input().split())) for _ in range(3)]

print("Enter goal state:")
goal = [list(map(int, input().split())) for _ in range(3)]

best_first_search(start, goal)
