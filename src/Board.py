from Move import Move


class Board:
    """Representation of current board state"""

    def __init__(self, boardstate, turn_player, our_color):
        self.boardstate = boardstate
        self.turn_player = turn_player
        self.our_color = our_color
        self.board_width = 8

    def get_legal_moves(self):
        """Return all legal moves"""

    def evaluate(self):
        """Evaluation function, return the eval score at current state.
           Should return -1, 1, or 0 at terminal boards."""
        pass

    def update(self, move):
        """Play new move and update board state"""
        pass

    def check_if_legal(self, move):
        """boolean, check if a given move is legal on the current board state"""
        lines = self.get_all_lines(move)
        for line in lines:
            if self.check_if_line_legal(line):
                return True
        return False

    def print_board(self):
        """Print the full board"""
        for i in range(8):
            print(self.boardstate[8*i:8*(i+1)])
        print()

    def get_all_lines(self, move):
        all_lines = []
        board_width = self.board_width
        pos = move.location
        row = pos // board_width
        col = pos % board_width

        """Get all lines in every direction"""
        # Foward and Bacwards, the easy ones -------------------------------------------------------------
        forward = []
        current_col = col + 1
        while current_col <= board_width - 1:
            index = (board_width*row) + current_col
            forward.append(index)
            current_col = current_col + 1
        # print(forward)
        all_lines.append(forward)
        backward = []
        current_col = col - 1
        while current_col >= 0:
            index = (board_width*row) + current_col
            backward.append(index)
            current_col = current_col - 1
        # print(backward)
        all_lines.append(backward)
        # Up and down, less easy ----------------------------------------------------------------------------
        up = []
        current_row = row - 1
        while current_row >= 0:
            index = (board_width*current_row) + col
            up.append(index)
            current_row = current_row - 1
        # print(up)
        all_lines.append(up)
        down = []
        current_row = row + 1
        while current_row <= board_width - 1:
            index = (board_width*current_row) + col
            down.append(index)
            current_row = current_row + 1
        # print(down)
        all_lines.append(down)
        # Forward Diagonals, same idea -----------------------------------------------------------------------
        forward_up_diagonal = []
        current_row = row - 1
        current_col = col + 1
        while current_row >= 0 and current_col <= board_width - 1:
            index = (board_width*current_row) + current_col
            forward_up_diagonal.append(index)
            current_row = current_row - 1
            current_col = current_col + 1
        # print(forward_up_diagonal)
        all_lines.append(forward_up_diagonal)
        forward_down_diagonal = []
        current_row = row + 1
        current_col = col + 1
        while current_row <= board_width - 1 and current_col <= board_width - 1:
            index = (board_width*current_row) + current_col
            forward_down_diagonal.append(index)
            current_row = current_row + 1
            current_col = current_col + 1
        # print(forward_down_diagonal)
        all_lines.append(forward_down_diagonal)
        # Backward diagonals, same idea -------------------------------------------------------------------
        backward_up_diagonal = []
        current_row = row - 1
        current_col = col - 1
        while current_row >= 0 and current_col >= 0:
            index = (board_width*current_row) + current_col
            backward_up_diagonal.append(index)
            current_row = current_row - 1
            current_col = current_col - 1
        # print(backward_up_diagonal)
        all_lines.append(backward_up_diagonal)
        backward_down_diagonal = []
        current_row = row + 1
        current_col = col - 1
        while current_row <= board_width - 1 and current_col >= 0:
            index = (board_width*current_row) + current_col
            backward_down_diagonal.append(index)
            current_row = current_row + 1
            current_col = current_col - 1
        # print(backward_down_diagonal)
        all_lines.append(backward_down_diagonal)
        return all_lines

    def check_if_line_legal(self, line):
        vals = [self.boardstate[index] for index in line]
        # print(vals)
        try:
            index = vals.index(self.our_color)
            # print(index)
        except ValueError:
            # print("item not present")
            return False
        between = vals[:index]
        # print(between)
        if len(between) == 0 or 0 in between:
            return False
        return True


class NewBoard(Board):
    """Make the board at the start of the game"""

    def __init__(self, ourcolor):
        boardstate = [0] * 64
        boardstate[27], boardstate[28] = -1, 1
        boardstate[35], boardstate[36] = 1, -1
        super().__init__(boardstate, 1, ourcolor)
