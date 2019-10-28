# Sudoku-spill

board = []


def initialize_board():
    box = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(9):
        board.append(box)


def print_board():
    line = "  +-------+-------+-------+"
    count = 0

    print("    0 1 2   3 4 5   6 7 8")
    print(line)
    # for entry in board:
    #     print(count, end="")
    #     for column in entry:
    #         for row in entry:
    #             for value in row:
    #                 print(value, end="")
    #     count += 1


def valid_number(n):
    try:
        n = int(n)
        if n > 0 and n <= 9:
            return True
        else:
            return False
    except ValueError:
        return False


initialize_board()
print_board()