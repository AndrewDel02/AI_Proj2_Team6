class Minimax:
    def __init__(self):
        self.alpha = 0
        self.beta = 0
        self.queue = []
        self.board_dict = {}  # boardstate = key, score = val

    def decide(self, time, board):
        """Find and return the best move for a given board within a give time"""
        pass

    def evaluate_board(self, board):
        """Calculates the score of the given board state"""
        pass