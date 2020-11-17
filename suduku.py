board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,2,0,0,0,5,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,7,0,0,0]
    ]

def print_board(board):
    for line in board:
        print(line)
    print()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(num, sqr, board):
    #check if valid row:
    for col in range(len(board[0])):
        if board[sqr[0]][col] == num and sqr[1] != col:
            return False

    #check if valid col:
    for row in range(len(board)):
        if board[row][sqr[1]] == num and sqr[0] != row:
            return False

    #check box:
    box = [sqr[0] // 3, sqr[1] // 3]
    for i in range (box[0] * 3, box[0] * 3 + 3):
        for j in range (box[1] * 3, box[1] * 3 + 3):
            if board[i][j] == num and i != sqr[0] and j != sqr[1]:
                return False

    return True

def solve(board):
    if find_empty(board) == None:
        return True
    else:
        row, col = find_empty(board)

        for i in range (1, 10):
            if is_valid(i, (row, col), board):
                board[row][col] = i

                if solve(board):
                    return True

                board[row][col] = 0

        return False





def main():
    print_board(board)
    solve(board)
    print_board(board)



if __name__ == '__main__':
    main()
