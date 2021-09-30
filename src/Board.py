import copy
from Move import Move
import exceptions


class Board:
    """Representation of current board state"""

    def __init__(self, boardstate, turn_player, our_color):
        self.boardstate = boardstate
        self.turn_player = turn_player
        self.our_color = our_color
        self.board_width = 8

    def get_legal_moves(self):
        """Return all legal moves"""
        legal_moves = []
        for index in range(self.board_width ** 2):
            possible_move = Move(index, self.turn_player)
            if self.check_if_legal(possible_move):
                legal_moves.append(possible_move)
        if len(legal_moves) == 0:  # to represent a pass if no legal moves found
            pass_move = Move(-1, self.turn_player)
            legal_moves.append(pass_move)
        return legal_moves

    def raw_score(self):
        """Evaluation function, return the eval score at current state.
           Should return total number of pieces that one player has over the other."""
        score = 0
        for boardstate in self.boardstate:
            score += boardstate
        return score

    def update(self, move):
        """Play new move and update board state"""
        newBoard = copy.deepcopy(self)
        # newBoard = Board(self.boardstate, self.turn_player, self.our_color)

        # if not newBoard.check_if_legal(move):
        #     raise exceptions.InvalidMoveException

        if move.location != -1:  # if not pass
            newBoard.boardstate[move.location] = move.turn_player  # add move

            # Update board
            lines = newBoard.get_all_lines(move)  # get all lines coming from location of the move
            # print(lines)
            for line in lines:  # iterate through lines
                # print(line)
                tail = newBoard.get_line_sandwich_tail(line, move.turn_player)
                # print(tail)
                if tail != -1:
                    finished = False
                    for index in line:  # get each board state in the line up to tail
                        if index == tail:
                            finished = True
                        if index != tail and not finished:
                            val = newBoard.boardstate[index]
                            if val != move.turn_player and val != 0:
                                newBoard.boardstate[index] = move.turn_player
        else:
            newBoard.turn_player = -1 if newBoard.turn_player == 1 else 1
        return newBoard

    def swap_board_sides(self):
        newBoard = copy.deepcopy(self)
        newBoard.turn_player = -1 if newBoard.turn_player == 1 else 1
        return newBoard

    def get_line_sandwich_tail(self, line, turn_player):
        """Checks what the closest sandwich is for the line: returns index of tail end of sandwich
         or -1 if no sandwich"""
        if len(line) < 2:
            return -1  # checks if line is too small to sandwich for quick exit of method
        for index in line:
            val = self.boardstate[index]
            if val == 0:  # handles for illegal moves, mostly for development
                return -1
            if val == turn_player:
                return index  # closest sandwich is accepted as per rules, and lines go from closest to furthest
        return -1  # should only get here if no sandwich

    def check_if_legal(self, move):
        """boolean, check if a given move is legal on the current board state"""
        if move.turn_player != self.turn_player:
            return False
        if self.boardstate[move.location] != 0:  # make sure spot isn't taken already
            return False
        lines = self.get_all_lines(move)  # get all lines coming from location of the move
        # print(move.location)
        # print(lines)
        for line in lines:  # if any of the lines would result in flipping tiles, the move is legal
            if self.check_if_line_legal(line, self.turn_player):
                return True
        return False

    def print_board(self):
        """Print the full board"""
        for i in range(8):
            # print(self.boardstate[8 * i:8 * (i + 1)])
            output = str(i+1) + '\t'
            for j in range(8):
                output += (str(self.boardstate[8 * i + j]) + '\t')
            print(output)
        columns = "o\t"
        for i in range(8):
            columns += chr(i + 65) + '\t'
        print(columns)
        print()

    def get_all_lines(self, move):
        """Generates 8 lists of board indices representing the lines forward, backward, up, down, forward up diagonal,
           forward down diagonal, backward up diagonal, and backward down diagonal from the move location,
           all starting from the position closest to the move location and going outward."""
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
            index = (board_width * row) + current_col
            forward.append(index)
            current_col = current_col + 1
        # print(forward)
        all_lines.append(forward)
        backward = []
        current_col = col - 1
        while current_col >= 0:
            index = (board_width * row) + current_col
            backward.append(index)
            current_col = current_col - 1
        # print(backward)
        all_lines.append(backward)
        # Up and down, less easy ----------------------------------------------------------------------------
        up = []
        current_row = row - 1
        while current_row >= 0:
            index = (board_width * current_row) + col
            up.append(index)
            current_row = current_row - 1
        # print(up)
        all_lines.append(up)
        down = []
        current_row = row + 1
        while current_row <= board_width - 1:
            index = (board_width * current_row) + col
            down.append(index)
            current_row = current_row + 1
        # print(down)
        all_lines.append(down)
        # Forward Diagonals, same idea -----------------------------------------------------------------------
        forward_up_diagonal = []
        current_row = row - 1
        current_col = col + 1
        while current_row >= 0 and current_col <= board_width - 1:
            index = (board_width * current_row) + current_col
            forward_up_diagonal.append(index)
            current_row = current_row - 1
            current_col = current_col + 1
        # print(forward_up_diagonal)
        all_lines.append(forward_up_diagonal)
        forward_down_diagonal = []
        current_row = row + 1
        current_col = col + 1
        while current_row <= board_width - 1 and current_col <= board_width - 1:
            index = (board_width * current_row) + current_col
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
            index = (board_width * current_row) + current_col
            backward_up_diagonal.append(index)
            current_row = current_row - 1
            current_col = current_col - 1
        # print(backward_up_diagonal)
        all_lines.append(backward_up_diagonal)
        backward_down_diagonal = []
        current_row = row + 1
        current_col = col - 1
        while current_row <= board_width - 1 and current_col >= 0:
            index = (board_width * current_row) + current_col
            backward_down_diagonal.append(index)
            current_row = current_row + 1
            current_col = current_col - 1
        # print(backward_down_diagonal)
        all_lines.append(backward_down_diagonal)
        return all_lines

    def check_if_line_legal(self, line, turn_player):
        """Check if a line would result in flipping any tiles,
           Finds the closest matching tile and checks if the only thing
           between the move location and tile location are opposing tiles"""
        vals = [self.boardstate[index] for index in line]
        # print(vals)
        try:
            index = vals.index(turn_player)
            # print(index)
        except ValueError:
            # print("item not present")
            return False
        between = vals[:index]
        # print(between)
        if len(between) == 0 or 0 in between:
            return False
        return True

    @staticmethod
    def get_board_val(position):
        """Converts the referee's format of A-H + 1-8 to board's version of 0-63"""
        ascii = ord(position[0])
        row = int(position[2])
        if len(position) != 4:
            print("Not 3 characters")
            return -1
        elif 72 < ascii or ascii < 65:
            print("Invalid column")
            return -1
        elif 8 < row or row < 1:
            print("Invalid row")
            return -1
        else:
            return ascii - 65 + (row - 1) * 8


class NewBoard(Board):
    """Make the board at the start of the game"""

    def __init__(self, ourcolor):
        boardstate = [0] * 64
        boardstate[27], boardstate[28] = -1, 1
        boardstate[35], boardstate[36] = 1, -1
        super().__init__(boardstate, 1, ourcolor)
