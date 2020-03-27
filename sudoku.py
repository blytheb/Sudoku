# print sudoku puzzle nicely in terminal with box outline
def print_b(bo):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print('---------------------')
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print('| ', end="")
            if c == 8:
                print(bo[r][c])
            else:
                print(str(bo[r][c]) + " ", end="")


# finds the next empty spot to fill
# returns true if there is a empty square
def find_next_empty(bo, loc):
    for r in range(9):
        for c in range(9):
            if bo[r][c] == 0:
                loc[0] = r
                loc[1] = c
                return True
    return False


# checks to see if possible number is valid to be placed
# returns false if this num is in the same row, column, or box
# returns true if its a valid num for that spot
def is_valid(bo, row, col, num):
    for a in bo[row]:
        if num == a:
            return False
    for b in range(9):
        if num == bo[b][col]:
            return False
    cstart = (col // 3)*3
    rstart = (row // 3)*3
    for r in range(rstart, rstart+3):
        for c in range(cstart, cstart+3):
            if bo[r][c] == num:
                return False
    return True

# recursive to keep trying to fill empty squares with right numbers
def solve_sudoku(bo):
    loc = [0, 0]
    if not find_next_empty(bo, loc):
        return True
    row = loc[0]
    col = loc[1]
    for i in range(1, 10):
        if is_valid(bo, row, col, i):
            bo[row][col] = i
            if solve_sudoku(bo):
                return True
            bo[row][col] = 0
    return False


def main():
    matrix = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print_b(matrix)
    if solve_sudoku(matrix):
        print_b(matrix)
    else:
        print("no answer")


main()
