from collections import deque

class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def waterJug(jug1, jug2, target):
    q = deque()
    visited = set()

    q.append(State(0, 0))
    visited.add((0, 0))

    while q:
        cur = q.popleft()
        a, b = cur.x, cur.y
        print(f"({a},{b})")

        if a == target or b == target:
            print("Target reached!")
            return

        nextStates = [
            State(jug1, b),
            State(a, jug2),
            State(0, b),
            State(a, 0),
            State(max(0, a - (jug2 - b)), min(jug2, b + a)),
            State(min(jug1, a + b), max(0, b - (jug1 - a)))
        ]

        for ns in nextStates:
            if (ns.x, ns.y) not in visited:
                visited.add((ns.x, ns.y))
                q.append(ns)

    print("No solution found.")

def main():
    jug1, jug2, target = map(int, input("Enter capacity of jug1, jug2 and target: ").split())

    if target > max(jug1, jug2):
        print("Target cannot be greater than jug capacities.")
        return

    waterJug(jug1, jug2, target)

if __name__ == "__main__":
    main()
