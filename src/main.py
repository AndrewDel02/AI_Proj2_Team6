from Board import Board, NewBoard
from Move import Move
import timeit

def main():
    board = NewBoard(1)
    board.print_board()
    legal_moves = board.get_legal_moves()
    for move in legal_moves:
        print(move.convert_location_to_ref_representation())

    # runtime = timeit.timeit(board.get_legal_moves, number=10000)
    # print("runtime is " + str(runtime/10000))

    """Testing update function"""
    board.update(legal_moves[1])
    board.print_board()
    board.update(Move(25, -1))
    board.print_board()
    board.update(Move(29, -1))
    board.print_board()
    legal_moves = board.get_legal_moves()
    for move in legal_moves:
        print(move.convert_location_to_ref_representation())

    """Testing get_board_val and also multiple line capture"""
    board.update(Move(board.get_board_val("E3"), -1))
    board.print_board()
    board.update(Move(board.get_board_val("F3"), 1))
    board.print_board()
    board.update(Move(board.get_board_val("D3"), 1))
    board.print_board()

    score = board.evaluate()
    print("Score is " + str(score))

if __name__ == '__main__':
    main()
