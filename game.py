
# print sudoku puzzle nicely in terminal with box outline
def print_b(bo, size, box):
    for r in range(size):
        if r % box == 0 and r != 0:
            print('---------------------')
        for c in range(size):
            if c % box == 0 and c != 0:
                print('| ', end="")
            if c == size - 1:
                print(bo[r][c])
            else:
                print(str(bo[r][c]) + " ", end="")


# finds the next empty spot to fill
# returns true if there is a empty square
def find_next_empty(bo, size, loc):
    for r in range(size):
        for c in range(size):
            if bo[r][c] == 0:
                loc[0] = r
                loc[1] = c
                return True
    return False


# checks to see if possible number is valid to be placed
# returns false if this num is in the same row, column, or box
# returns true if its a valid num for that spot
def is_valid(bo, size, box, row, col, num):
    for a in bo[row]:
        if num == a:
            return False
    for b in range(size):
        if num == bo[b][col]:
            return False
    cstart = (col // box)*box
    rstart = (row // box)*box
    for r in range(rstart, rstart+box):
        for c in range(cstart, cstart+box):
            if bo[r][c] == num:
                return False
    return True


# recursive to keep trying to fill empty squares with right numbers
def solve_sudoku(bo, size, box):
    loc = [0, 0]
    if not find_next_empty(bo, size, loc):
        return True
    row = loc[0]
    col = loc[1]
    for i in range(1, size + 1):
        if is_valid(bo, size, box, row, col, i):
            bo[row][col] = i
            if solve_sudoku(bo, size, box):
                return True
            bo[row][col] = 0
    return False


def main():
    size = 4
    box = 2
    matrix = [[int(x) for x in line.strip().split(' ')] for line in open('easy4.txt')]
    print("This is what you start with:")
    print_b(matrix, size, box)
    if solve_sudoku(matrix, size, box):
        print("This is the final answer: ")
        print_b(matrix, size, box)
    else:
        print("no answer")


main()
