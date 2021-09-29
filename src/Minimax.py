from Board import Board
from Move import Move


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
        self.nodes_evaled = 0
        self.board_dict = {}  # boardstate = key, score = val

    def decide(self, time: float, board: Board, depth: int, our_color: int):
        """Find and return the best move for a given board within a give time"""
        if our_color == -1:
            val, move = self.get_min_value(board, depth, -99999999, 99999999)
        else:
            val, move = self.get_max_value(board, depth, -99999999, 99999999)

        return val, move

    def evaluate_board(self, board: Board):
        """Calculates the move score of the given board state"""
        board_string = str(board.boardstate)
        if board_string in self.board_dict:
            return self.board_dict[board_string]

        score = board.raw_score()
        for i in range(64):  # iterate through each cell
            addition = 0  # what will be added to score
            val = board.boardstate[i]  # value of current cell
            if val != 0:  # skips everything if cell value is 0
                addition = Minimax.score_values[i]
                if val < 0:  # swaps value of addition if the side is -1
                    addition *= -1
            score += addition

        self.board_dict[board_string] = score
        return score

    def get_min_value(self, board: Board, depth: int, alpha: float, beta: float):
        """calculates the min value in the minimax tree"""

        # print("minimizing at depth: " + str(depth))
        worst = 9999999
        move_to_make = Move(-1, -1)

        if depth == 0:
            self.nodes_evaled += 1
            score = self.evaluate_board(board)
            # print("result is: " + str(score))
            return score, move_to_make

        for move in board.get_legal_moves():
            new_board = board.update(move)
            move_score, next_move = self.get_max_value(new_board, depth - 1, alpha, beta)
            if move_score < worst:
                worst = move_score
                move_to_make = move
                beta = min(beta, move_score)
            if worst <= alpha:
                return worst, move_to_make

        # print("result is: " + str(worst) + " at " + move_to_make.convert_location_to_ref_representation())
        return worst, move_to_make

    def get_max_value(self, board: Board, depth: int, alpha: float, beta: float):
        """calculates the max value in the minimax tree"""

        # print("maximizing at depth: " + str(depth))
        best = -9999999
        move_to_make = Move(-1, 1)

        if depth == 0:
            self.nodes_evaled += 1
            score = self.evaluate_board(board)
            # print("result is: " + str(score))
            return score, move_to_make

        for move in board.get_legal_moves():
            new_board = board.update(move)
            move_score, next_move = self.get_min_value(new_board, depth - 1, alpha, beta)
            if move_score > best:
                best = move_score
                move_to_make = move
                alpha = max(alpha, move_score)
            if best >= beta:
                return best, move_to_make

        # print("result is: " + str(best) + " at " + move_to_make.convert_location_to_ref_representation())
        return best, move_to_make
