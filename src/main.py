import sys
import time

from Board import Board, NewBoard
from Move import Move
import timeit
import argparse
from os.path import exists
import platform
import exceptions


def main():
    parser = argparse.ArgumentParser(description="Play Othello Better Than Anyone")
    parser.add_argument("ref_location", help="Location of the directory where the ref is")
    args = parser.parse_args(sys.argv[1:])

    name = "comp"
    our_color = -1  # default our color to white, then if we read a blank move file we change it
    opp_color = 1
    current_board = NewBoard(our_color)

    directory = args.ref_location
    limiter = '\\' if platform.system() == "Windows" else "/"
    directory = directory + limiter

    # Make sure we've been given the right directory by checking if the ref program exists in it
    if not exists(directory + "Referee.py"):
        print("No Referee Program in that directory")
        raise exceptions.CantFindRefException

    # Main Game Loop -----------------------------------------------------------------------
    while not exists(directory + "end_game"):
        if exists(directory + name + ".go"):  # our turn
            # Open the move file to read and write
            move_file = open(directory+"move_file", "r+")
            file_text = move_file.read()
            print(file_text)
            # first check if the move file is blank, if so we're black going first
            if file_text == "":
                current_board = NewBoard(1)
                our_color = 1
                opp_color = -1
                print("going first")
            else:  # otherwise get the move and update the board
                pos = file_text.split(" ", 1)[1]
                index = Board.get_board_val(pos)
                current_board.update(Move(index, opp_color))

            # This is where we make our move
            best_move = Move(19, our_color)  # this is replaced with result of minimax
            string_to_write = name + " " + best_move.convert_location_to_ref_representation()
            move_file.write(string_to_write)
            move_file.close()
            time.sleep(.1)  # let the ref update the board


if __name__ == '__main__':
    main()
