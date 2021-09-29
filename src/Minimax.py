from Board import Board
from Move import Move


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
        self.queue = []
        self.board_dict = {}  # boardstate = key, score = val

    def decide(self, time: float, board: Board):
        """Find and return the best move for a given board within a give time"""
        pass

    @staticmethod
    def evaluate_board(board: Board):
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

    def get_min_value(self, board: Board, depth: int, alpha: float, beta: float):
        """calculates the min value in the minimax tree"""
        if depth == 0:
            self.evaluate_board(board)
        
        worst = 9999999
        move_to_make = Move(-1, -1)

        for move in board.get_legal_moves():
            move_score, next_move = self.get_max_value(board.update(move), depth - 1, alpha, beta)
            if move_score < worst:
                worst = move_score
                move_to_make = move
                beta = min(beta, move_score)
            if worst <= alpha:
                return worst, move_to_make
        
        return worst, move_to_make

    def get_max_value(self, board: Board, depth: int, alpha: float, beta: float):
        """calculates the max value in the minimax tree"""
        if depth == 0:
            self.evaluate_board(board)
        
        best = -9999999
        move_to_make = Move(-1, 1)

        for move in board.get_legal_moves():
            move_score, next_move = self.get_min_value(board.update(move), depth - 1, alpha, beta)
            if move_score > best:
                best = move_score
                move_to_make = move
                alpha = max(alpha, move_score)
            if best >= beta:
                return best, move_to_make
        
        return best, move_to_make
