class Minimax:

    """The additional value we give to certain important locations"""
    score_values = [100, -10, 3, 2, 2, 3, -10, 100,
                    -10, -10, -1, -1, -1, -1, -10, -10,
                    3, -1, 1.5, 1, 1, 1.5, -1, 3,
                    2, -1, 1, 0, 0, 1, -1, 2,
                    2, -1, 1, 0, 0, 1, -1, 2,
                    3, -1, 1.5, 1, 1, 1.5, -1, 3,
                    -10, -10, -1, -1, -1, -1, -10, -10,
                    100, -10, 3, 2, 2, 3, -10, 100]

    def __init__(self):
        self.alpha = 0
        self.beta = 0
        self.queue = []
        self.board_dict = {}  # boardstate = key, score = val

    def decide(self, time, board):
        """Find and return the best move for a given board within a give time"""
        pass

    @staticmethod
    def evaluate_board(board):
        """Calculates the move score of the given board state"""
        score = board.raw_score()
        for i in range(64):  # iterate through each cell
            addition = 0  # what will be added to score
            val = board.boardstate[i]  # value of current cell
            if val != 0:  # skips everything if cell value is 0
                addition = Minimax.score_values[i]
                if val < 0:  # swaps value of addition if the side is -1
                    addition *= -1
            score += addition
        return score
