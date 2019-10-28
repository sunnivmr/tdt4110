
values = []


def initialize():
    for i in range(3):
        row = [" ", " ", " "]
        values.append(row)


def set_value(row, column, value):
    try:
        row = int(row)
        column = int(column)
        values[row][column] = value
    except ValueError:
        print("Ugyldig verdi.")


def print_board():
    print("  0     1     2  ")
    print("  -------------")
    print("0 |", values[0][0], "|", values[0][1], "|", values[0][2], "|")
    print("  -------------")
    print("1 |", values[1][0], "|", values[1][1], "|", values[1][2], "|")
    print("  -------------")
    print("2 |", values[2][0], "|", values[2][1], "|", values[2][2], "|")
    print("  -------------")


def set_playerx(name):
    return 'x'


def set_playero(name):
    return 'o'


def is_valid(row, column):
    valid = [0, 1, 2]
    try:
        row = int(row)
        column = int(column)
    except ValueError:
        print("Ugyldig verdi.")
    if row in valid and column in valid and values[row][column] == " ":
        return True
    else:
        print("Ugyldig trekk, prøv igjen.")
        return False


def gameround(player, player_name):

    print(player_name, "(", player, ") sin tur:")
    rad = input("Rad: ")
    kolonne = input("Kolonne: ")
    valid = False
    while not isfinished():
        if is_valid(rad, kolonne):
            valid = True
            set_value(rad, kolonne, player)
            print_board()
        else:
            print("Ugyldig verdi, prøv igjen.")


def game(x, o, x_name, o_name):

    turn = x

    while not isfinished():
        if turn == x:
            print(x_name, "(", x, ") sin tur:")
        else:
            print(o_name, "(", o, ") sin tur:")
        rad = input("Rad: ")
        kolonne = input("Kolonne: ")
        if is_valid(rad,kolonne):
            if turn==x:
                set_value(rad, kolonne, x)
                turn = o
            else:
                set_value(rad, kolonne, o)
                turn = x
            print_board()
        else:
            print(" ")


def isfinished():
    return False


def main():

    initialize()

    print("--------------------")
    print("\nVelkommen til tre på rad!\n")
    print("--------------------")

    playerx_name = input("Navn på player x: ")
    playero_name = input("Navn på player o: ")

    playerx = set_playerx(playerx_name)
    playero = set_playero(playero_name)

    print(playerx_name, "er", playerx, "og", playero_name, "er", playero, "\n")

    print_board()
    game(playerx, playero, playerx_name, playero_name)



main()

