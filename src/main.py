from Board import Board, NewBoard
from Move import Move

def main():
    board = NewBoard(1)
    board.print_board()
    test_move = Move(9, 1)
    x = board.check_if_legal(test_move)
    print(x)

if __name__ == '__main__':
    main()