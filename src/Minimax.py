class Minimax:

    """The additional value we give to certain important locations"""
    score_values = [3, -2, 2, 2, 2, 2, -2, 3,
                    -2, -2, -1, -1, -1, -1, -2, -2,
                    2, -1, 1.5, 1, 1, 1.5, -1, 2,
                    2, -1, 1, 0, 0, 1, -1, 2,
                    2, -1, 1, 0, 0, 1, -1, 2,
                    2, -1, 1.5, 1, 1, 1.5, -1, 2,
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

    @staticmethod
    def evaluate_board(board):
        """Calculates the move score of the given board state"""
        score = board.raw_score()
        for i in range(64):  # iterate through each cell
            addition = 0  # what will be added to score
            val = board.boardstate[i]  # value of current cell
            if val != 0:  # skips everything if cell value is 0
                addition = 2 * Minimax.score_values[i]
                if val < 0:  # swaps value of addition if the side is -1
                    addition *= -1
            score += addition
        return score

    def getMinValue(board, depth, self) :
        """calculates the min value in the minimax tree"""
        if depth == 0 :
            self.evaluate_board(board)
        
        worst = -9999999

        for Move in board.get_legal_moves:
            moveScore = self.getMaxValue(board.update(board, Move), depth-1, self)
            worst = min(worst, moveScore)
            self.beta = min(self.beta, moveScore)
            if self.beta <= self.alpha:
                return worst
        
        return worst


    def getMaxValue(board, depth, self) :
        """calculates the max value in the minimax tree"""
        if depth == 0:
                self.evaluate_board(board)
        
        best = 9999999

        for Move in board.get_legal_moves:
            moveScore = self.getMinValue(board.update(board, Move), depth-1, self)
            best = max(best, moveScore)
            self.alpha = max(self.alpha, moveScore)
            if self.beta <= self.alpha:
                return best
        
        return best
