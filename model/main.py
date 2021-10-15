from model.board import Board, Tile

def display_board(board):
    for row in board:  # for i in range(len(board))
        for item in row: # for j in range(len(board[i])
            print(item, end=' ') #board[i][j]
        print()

def main():
    board = Board()
    board2 = Board()
    #print(board._matrix)
    display_board(board.get_board())
    board.play()
    board2.play()

    play(board, 2, 1, )

if __name__ == '__main__':
    main()
    """
    lst = []
    for val in range(1, 11):
        lst.append(val)
    """
    lst = [val for val in range(1, 11)]
    print(lst)

    m = [[Tile.EMPTY for _ in range(10)] for _ in range(10)]
    print(m)