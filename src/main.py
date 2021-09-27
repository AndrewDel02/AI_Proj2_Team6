from Board import Board, NewBoard
from Move import Move
import timeit

def main():
    board = NewBoard(1)
    board.print_board()
    legal_moves = board.get_legal_moves()
    for move in legal_moves:
        print(move.location)

    runtime = timeit.timeit(board.get_legal_moves, number=10000)
    print("runtime is " + str(runtime/10000))


if __name__ == '__main__':
    main()
