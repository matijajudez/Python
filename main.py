
import random

#FUNCKIJE
#display board je funkcija za prikaz borda za igro
def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

    return board

#Player input izve igralčev marker X ali O
def player_input():
    marker = ""

    while marker != 'X' and marker != "O":
        marker = input("Player 1 please, choose X or O: ").upper()

    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)

#funkcija naredi nov bord na podlagi, boarda, markerja, ki je lahko igralec 1 ali 2 in pa glede pozicije (input)
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    coin_flip = random.randint(0, 1)

    if coin_flip == 0:
        return 1
    else:
        return 2


def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Izberite naslednjo pozicijo:"))

    return position



def replay():
    choice = input("Ali želite igrati šeenkrat? (da/ne): ").upper()

    return choice == "DA"



#DEJANSKA KODA

print("\nWelcome to the Križec Krožeč game.")
print("Here is the board of the game:\n")

while True:
    board = [" "] * 10
    display_board(board)
    print("\nBefore we continue please choose your marker (X and O).")
    player1_marker, player2_marker = player_input()
    print(f"Igralec 1 ima marker {player1_marker}\nIgralec 2 ima marker {player2_marker}")
    turn = choose_first()

    if turn == 1:
        print(f"Prvi na vrsti je igralec 1. Vaš marker je {player1_marker}")
    else:
        print(f"Prvi na vrsti je igralec 2. Vaš marker je {player2_marker}")

    play_game = input("Ali ste pripravljeni igrati? (da,ne): ")

    if play_game == "da":
        game_on = True
    else:
        game_on = False
        break

    while game_on:
        if turn == 1:

            #na vrsti je igralec 1
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)


            if win_check(board,player1_marker):
                display_board(board)
                print("ČESTITAMO! Zmagali ste igro! ")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Igra je izenačena")
                    break
                else:
                    turn = 2
        else:
            #igralec 2
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("ČESTITAMO! Zmagali ste igro! ")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Igra je izenačena")
                    break
                else:
                    turn = 1
    if not replay():
        break