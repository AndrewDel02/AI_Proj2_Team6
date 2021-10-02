import sys
import time
from src.Board import Board, NewBoard
from src.Move import Move
import argparse
from os.path import exists
import platform
import src.exceptions as exceptions
from src.Minimax import Minimax


def main():
    # # Manual Play Mode ----------------------------------------------------------------------
    # print("AI Black y/n?")
    # our_color = 1 if input() == "y" else -1
    # opp_color = -1 if our_color == 1 else 1
    # current_board = NewBoard(our_color)
    # current_turn = 1
    # minimax = Minimax()
    # time_limit = 5.0
    #
    # while True:
    #     if current_turn == our_color:
    #         print("Finding move")
    #         best_score, best_move, depth_searched = minimax.decide(time_limit, current_board, our_color)
    #         print()
    #         print("Results -----------------------------------------")
    #         print("Depth Analyzed: " + str(depth_searched))
    #         print("Best move: " + best_move.convert_location_to_ref_representation())
    #         print("Best score: " + str(best_score))
    #         print("Nodes analyzed: " + str(minimax.nodes_evaled))
    #         print("-------------------------------------------------")
    #         current_board = current_board.update(best_move)
    #         current_turn = 1 if current_turn == -1 else -1
    #     else:
    #         print("Opp Move: ")
    #         opp_move = input()
    #         index = Board.get_board_val(opp_move)
    #         current_board = current_board.swap_board_sides()
    #         current_board.update(Move(index, opp_color))
    #         current_turn = 1 if current_turn == -1 else -1

    # Standard Ref Mode ---------------------------------------------------------------------
    minimax = Minimax()

    name = "confusedChessBot"
    our_color = -1  # default our color to white, then if we read a blank move file we change it
    opp_color = 1
    current_board = NewBoard(our_color)

    # Make sure we've been given the right directory by checking if the ref program exists in it
    if not exists("Referee.py"):
        print("No Referee Program in this directory")
        raise exceptions.CantFindRefException

    # Main Game Loop -----------------------------------------------------------------------
    while not exists("end_game"):
        if exists(name + ".go"):  # our turn
            # Open the move file to read and write
            move_file = open("move_file", "r+")
            file_text = ""
            for next_line in move_file.readlines():
                if next_line.isspace():
                    break
                else:
                    file_text = next_line
            # print(file_text)
            # first check if the move file is blank, if so we're black going first
            if file_text == "":
                current_board = NewBoard(1)
                our_color = 1
                opp_color = -1
                print("going first")
            else:  # otherwise get the move and update the board
                # Get last non-empty line from file
                line = ""
                pos = file_text.split(" ", 1)[1]
                index = Board.get_board_val(pos)
                current_board = current_board.swap_board_sides()
                current_board = current_board.update(Move(index, opp_color))
                # current_board.print_board()

            # This is where we make our move
            best_val, best_move, depth_searched = minimax.decide(10.0, current_board, our_color)
            print()
            print("Results: ------------------------------------------")
            print("Best Move: " + best_move.convert_location_to_ref_representation())
            print("Depth Searched: " + str(depth_searched))
            print("Total Nodes Evaled: " + str(minimax.nodes_evaled))

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
