def game_field():
    for row in field:
        print(row)


def field_update(x, y):
    field[x][y] = "x" if player == 1 else "o"



def error_count(x, y):
    if x > 2 or y > 2:
        print("Invalid value: x or y needs to be less than 3")
        error = True
    elif x < 0 or y < 0:
        print("Invalid value: x or y needs to be positive")
        error = True
    elif field[x][y] != "-":
        print("Invalid value: position already occupied")
        error = True
    else:
        error = False
    return error


def win_check():
    for row in field:
        if set(row) == {"x"} or set(row) == {"o"}:
            print(f"Player number {player} won!")
            return True
    for i in range(3):
        if set([field[0][i], field[1][i], field[2][i]]) == {"x"} or set([field[0][i], field[1][i], field[2][i]]) == {"o"}:
            print(f"Player number {player} won!")
            return True
    if set([field[0][0], field[1][1], field[2][2]]) == {"x"} or set([field[0][0], field[1][1], field[2][2]]) == {"o"}:
        print(f"Player number {player} won!")
        return True
    if set([field[0][2], field[1][1], field[2][0]]) == {"x"} or set([field[0][2], field[1][1], field[2][0]]) == {"o"}:
        print(f"Player number {player} won!")
        return True
    if "-" not in field[0] and "-" not in field[1] and "-" not in field[2]:
        print("Draw!")
        return True
    return False



error = False
player = 1
field = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("Each turn use this format for your turn, every entry is divided by space: row number (counting from 0), column number (counting from 0).")


while True:
    if not error:
        game_field()
    if player == 1:
        turn_entry = input("First player (using x), input coordinates of your turn: ")
        x, y = turn_entry.split()
        x, y = int(x), int(y)
        error = error_count(x, y)
        if not error:
            field_update(x, y)
    else:
        turn_entry = input("Second player (using o), input coordinates of your turn: ")
        x, y = turn_entry.split()
        x, y = int(x), int(y)
        error = error_count(x, y)
        if not error:
            field_update(x, y)
    if win_check():
        game_field()
        break
    if not error:
        player = 3 - player

