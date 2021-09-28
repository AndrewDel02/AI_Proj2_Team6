class Minimax:

    """The additional value we give to certain important locations"""
    score_values = [3, -2, 2, 2, 2, 2, -2, 3,
                    -2, -2, -1, -1, -1, -1, -2, -2,
                    2, -1, 2, 2, 2, 2, -1, 2,
                    2, -1, 2, 0, 0, 2, -1, 2,
                    2, -1, 2, 0, 0, 2, -1, 2,
                    2, -1, 2, 2, 2, 2, -1, 2,
                    -2, -2, -1, -1, -1, -1, -2, -2,
                    3, -2, 2, 2, 2, 2, -2, 3]

    def __init__(self):
        self.alpha = 0
        self.beta = 0
        self.queue = []
        self.board_dict = {}  # boardstate = key, score = val

    def decide(self, time, board):
        """Find and return the best move for a given board within a give time"""
        pass

    def evaluate_board(self, board):
        """Calculates the move score of the given board state"""
        score = board.raw_score()
        for i in range(64):  # iterate through each cell
            addition = 0  # what will be added to score
            val = board.boardstate[i]  # value of current cell
            if val != 0:  # skips everything if cell value is 0
                addition = self.score_values[i]
                if val < 0:  # swaps value of addition if the side is -1
                    addition *= -1
            score += addition
        return score
