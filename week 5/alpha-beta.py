class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.player = 'X'

    def winner(self, p):
        b = self.board
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        return any(b[a] == b[b1] == b[c] == p for a, b1, c in wins)

    def full(self):
        return ' ' not in self.board

    def moves(self):
        return [i for i, v in enumerate(self.board) if v == ' ']

    def play(self, i):
        self.board[i] = self.player
        self.player = 'O' if self.player == 'X' else 'X'

    def undo(self, i):
        self.board[i] = ' '
        self.player = 'O' if self.player == 'X' else 'X'


def minimax(g, alpha, beta, maxing):
    if g.winner('O'):
        return 1
    if g.winner('X'):
        return -1
    if g.full():
        return 0

    if maxing:
        best = -1e9
        for m in g.moves():
            g.play(m)
            best = max(best, minimax(g, alpha, beta, False))
            g.undo(m)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1e9
        for m in g.moves():
            g.play(m)
            best = min(best, minimax(g, alpha, beta, True))
            g.undo(m)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def best_move(g):
    best = -1e9
    move = None
    for m in g.moves():
        g.play(m)
        score = minimax(g, -1e9, 1e9, False)
        g.undo(m)
        if score > best:
            best = score
            move = m
    return move


g = TicTacToe()

while True:
    print(g.board[0:3], "\n", g.board[3:6], "\n", g.board[6:9], "\n")

    if g.winner('X'):
        print("You win")
        break
    if g.winner('O'):
        print("AI wins")
        break
    if g.full():
        print("Draw")
        break

    if g.player == 'X':
        g.play(int(input("Move (0-8): ")))
    else:
        g.play(best_move(g))
