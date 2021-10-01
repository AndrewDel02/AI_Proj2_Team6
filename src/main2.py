import sys
import time
from Board import Board, NewBoard
from Move import Move
import argparse
from os.path import exists
import platform
import exceptions
from Minimax import Minimax


def main():
    parser = argparse.ArgumentParser(description="Play Othello Better Than Anyone")
    parser.add_argument("ref_location", help="Location of the directory where the ref is")
    args = parser.parse_args(sys.argv[1:])
    minimax = Minimax()

    name = "comp2"
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
            file_text = ""
            for next_line in move_file.readlines():
                if next_line.isspace():
                    break
                else:
                    file_text = next_line
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
                current_board = current_board.swap_board_sides()
                current_board = current_board.update(Move(index, opp_color))
                current_board.print_board()

            # This is where we make our move
            best_val, best_move, depth_searched = minimax.decide(10.0, current_board, our_color)
            print(best_move.convert_location_to_ref_representation())

            string_to_write = name + " " + best_move.convert_location_to_ref_representation() + '\n'
            move_file.write(string_to_write)
            move_file.close()
            current_board = current_board.update(best_move)
            current_board = current_board.swap_board_sides()
            time.sleep(.1)  # let the ref update the board

    """Testing MinMax"""
    # board = NewBoard(-1)
    # board = board.update(Move(19, 1))
    # time_limit = 10.0
    # minimax = Minimax()
    #
    # start_time = time.time()
    # best_score, best_move, depth_searched = minimax.decide(time_limit, board, -1)
    # end_time = time.time()
    # total_time = end_time - start_time
    # print()
    # print("Results -----------------------------------------")
    # print("Turn Player: White")
    # print("Depth Analyzed: " + str(depth_searched))
    # print("Best move: " + best_move.convert_location_to_ref_representation())
    # print("Best score: " + str(best_score))
    # print("Time Taken: " + str(total_time))
    # print("Nodes analyzed: " + str(minimax.nodes_evaled))
    # print("Time Per Node: " + str(total_time / minimax.nodes_evaled))
    # print("Unique Nodes: " + str(len(minimax.board_dict)))
    # print("Duplicate Nodes: " + str(minimax.dup_nodes))
    # print("-------------------------------------------------")
    #
    # new_board = board.update(best_move)
    # start_time = time.time()
    # best_score, best_move, depth_searched = minimax.decide(time_limit, new_board, 1)
    # end_time = time.time()
    # total_time = end_time - start_time
    # print()
    # print("Second Results -----------------------------------------")
    # print("Turn Player: Black")
    # print("Depth Analyzed: " + str(depth_searched))
    # print("Best move: " + best_move.convert_location_to_ref_representation())
    # print("Best score: " + str(best_score))
    # print("Time Taken: " + str(total_time))
    # print("Nodes analyzed: " + str(minimax.nodes_evaled))
    # print("Time Per Node: " + str(total_time / minimax.nodes_evaled))
    # print("Unique Nodes: " + str(len(minimax.board_dict)))
    # print("Duplicate Nodes: " + str(minimax.dup_nodes))
    # print("-------------------------------------------------")


if __name__ == '__main__':
    main()
