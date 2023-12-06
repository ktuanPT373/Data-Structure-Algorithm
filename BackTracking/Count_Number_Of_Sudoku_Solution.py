# board = [[0,0,3,4,0,0,0,8,9],
#          [0,0,6,7,8,9,0,2,3],
#          [0,8,0,0,2,3,4,5,6],
#          [0,0,4,0,6,5,0,9,7],
#          [0,6,0,0,9,0,0,1,4],
#          [0,0,7,2,0,4,3,6,5],
#          [0,3,0,6,0,2,0,7,8],
#          [0,0,0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0,0,0]]
# def constraint(i, j, v):
#     if board[i][j] == 0:
#         for a in range(3 * (j // 3), 3 * (j // 3) + 3):
#             for b in range(3 * (i // 3), 3 * (i // 3) + 3):
#                 if board[a][b] == v:
#                     return False
#         for a in range(i):
#             if board[a][j] == v:
#                 return False
#         for b in range(j):
#             if board[i][b] == v:
#                 return False
#         return True
#     return False

# def backtrack(i,j):
#     for v in range(1,10):
#         if constraint(i,j,v):
#             board[i][j] = v
#             if i == 8 and j == 8:
#                 print(board)
#             else:
#                 if j == 8:
#                     backtrack(i+1,0)
#                 else:
#                     backtrack(i,j+1)
# backtrack(0,0)
# print(count)
board = []
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True
def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return 1 
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                global count
                count += 1
            board[row][col] = 0
    return 0

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
count = 0
solve_sudoku(board)
print(count)
