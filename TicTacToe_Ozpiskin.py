"Projet TicTacToe"
"Ilham El Amriti et Derin Ozpiskin"

import random

board1 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board2 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board3 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board4 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board5 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board6 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board7 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board8 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
board9 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

board_de_jeu = [[board1, board2, board3],
                [board4, board5, board6],
                [board7, board8, board9]]

val = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9",
       "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9",
       "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
       "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
       "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9",
       "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9",
       "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
       "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9",
       "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"]

haut_gauche = ["A1", "A4", "A7", "D1", "D4", "D7", "G1", "G4", "G7"]
haut_centre = ["A2", "A5", "A8", "D2", "D5", "D8", "G2", "G5", "G8"]
haut_droite = ["A3", "A6", "A9", "D3", "D6", "D9", "G3", "G6", "G9"]
centre_gauche = ["B1", "B4", "B7", "E1", "E4", "E7", "H1", "H4", "H7"]
centre_centre = ["B2", "B5", "B8", "E2", "E5", "E8", "H2", "H5", "H8"]
centre_droite = ["B3", "B6", "B9", "E3", "E6", "E9", "H3", "H6", "H9"]
bas_gauche = ["C1", "C4", "C7", "F1", "F4", "F7", "I1", "I4", "I7"]
bas_centre = ["C2", "C5", "C8", "F2", "F5", "F8", "I2", "I5", "I8"]
bas_droite = ["C3", "C6", "C9", "F3", "F6", "F9", "I3", "I6", "I9"]

b1 = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
b2 = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
b3 = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
b4 = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
b5 = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
b6 = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
b7 = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
b8 = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
b9 = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]

ancienne_pos = []
game_still_on = True
old_games = []
ancienne_pos2 = []
def printBoard():
    print("    1  2  3 ||| 4  5  6 ||| 7  8  9  ")
    print("  A", end=" ")

    print(board_de_jeu[0][0][0][0] + ", " + board_de_jeu[0][0][0][1] + ", " + board_de_jeu[0][0][0][2], end=" ||| ")
    print(board_de_jeu[0][1][0][0] + ", " + board_de_jeu[0][1][0][1] + ", " + board_de_jeu[0][1][0][2], end=" ||| ")
    print(board_de_jeu[0][2][0][0] + ", " + board_de_jeu[0][2][0][1] + ", " + board_de_jeu[0][2][0][2])
    print("   _________________________________")

    print("  B", end=" ")
    print(board_de_jeu[0][0][1][0] + ", " + board_de_jeu[0][0][1][1] + ", " + board_de_jeu[0][0][1][2], end=" ||| ")
    print(board_de_jeu[0][1][1][0] + ", " + board_de_jeu[0][1][1][1] + ", " + board_de_jeu[0][1][1][2], end=" ||| ")
    print(board_de_jeu[0][2][1][0] + ", " + board_de_jeu[0][2][1][1] + ", " + board_de_jeu[0][2][1][2])
    print("   _________________________________")

    print("  C", end=" ")
    print(board_de_jeu[0][0][2][0] + ", " + board_de_jeu[0][0][2][1] + ", " + board_de_jeu[0][0][2][2], end=" ||| ")
    print(board_de_jeu[0][1][2][0] + ", " + board_de_jeu[0][1][2][1] + ", " + board_de_jeu[0][1][2][2], end=" ||| ")
    print(board_de_jeu[0][2][2][0] + ", " + board_de_jeu[0][2][2][1] + ", " + board_de_jeu[0][2][2][2])
    print("------------------------------------")
    print("")
    print("------------------------------------")

    print("  D", end=" ")
    print(board_de_jeu[1][0][0][0] + ", " + board_de_jeu[1][0][0][1] + ", " + board_de_jeu[1][0][0][2], end=" ||| ")
    print(board_de_jeu[1][1][0][0] + ", " + board_de_jeu[1][1][0][1] + ", " + board_de_jeu[1][1][0][2], end=" ||| ")
    print(board_de_jeu[1][2][0][0] + ", " + board_de_jeu[1][2][0][1] + ", " + board_de_jeu[1][2][0][2])
    print("   _________________________________")

    print("  E", end=" ")
    print(board_de_jeu[1][0][1][0] + ", " + board_de_jeu[1][0][1][1] + ", " + board_de_jeu[1][0][1][2], end=" ||| ")
    print(board_de_jeu[1][1][1][0] + ", " + board_de_jeu[1][1][1][1] + ", " + board_de_jeu[1][1][1][2], end=" ||| ")
    print(board_de_jeu[1][2][1][0] + ", " + board_de_jeu[1][2][1][1] + ", " + board_de_jeu[1][2][1][2])
    print("   _________________________________")

    print("  F", end=" ")
    print(board_de_jeu[1][0][2][0] + ", " + board_de_jeu[1][0][2][1] + ", " + board_de_jeu[1][0][2][2], end=" ||| ")
    print(board_de_jeu[1][1][2][0] + ", " + board_de_jeu[1][1][2][1] + ", " + board_de_jeu[1][1][2][2], end=" ||| ")
    print(board_de_jeu[1][2][2][0] + ", " + board_de_jeu[1][2][2][1] + ", " + board_de_jeu[1][2][2][2])
    print("------------------------------------")
    print("")
    print("------------------------------------")

    print("  G", end=" ")
    print(board_de_jeu[2][0][0][0] + ", " + board_de_jeu[2][0][0][1] + ", " + board_de_jeu[2][0][0][2], end=" ||| ")
    print(board_de_jeu[2][1][0][0] + ", " + board_de_jeu[2][1][0][1] + ", " + board_de_jeu[2][1][0][2], end=" ||| ")
    print(board_de_jeu[2][2][0][0] + ", " + board_de_jeu[2][2][0][1] + ", " + board_de_jeu[2][2][0][2])
    print("   _________________________________")

    print("  H", end=" ")
    print(board_de_jeu[2][0][1][0] + ", " + board_de_jeu[2][0][1][1] + ", " + board_de_jeu[2][0][1][2], end=" ||| ")
    print(board_de_jeu[2][1][1][0] + ", " + board_de_jeu[2][1][1][1] + ", " + board_de_jeu[2][1][1][2], end=" ||| ")
    print(board_de_jeu[2][2][1][0] + ", " + board_de_jeu[2][2][1][1] + ", " + board_de_jeu[2][2][1][2])
    print("   _________________________________")

    print("  I", end=" ")
    print(board_de_jeu[2][0][2][0] + ", " + board_de_jeu[2][0][2][1] + ", " + board_de_jeu[2][0][2][2], end=" ||| ")
    print(board_de_jeu[2][1][2][0] + ", " + board_de_jeu[2][1][2][1] + ", " + board_de_jeu[2][1][2][2], end=" ||| ")
    print(board_de_jeu[2][2][2][0] + ", " + board_de_jeu[2][2][2][1] + ", " + board_de_jeu[2][2][2][2])
    print("")
    print("")


def update_board(position, value):
    row_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    col_map = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8}

    # Nous extrayons la position entrée par l'utilisateur.
    row_letter = position[0]  # comme  "A", "B", "C"
    col_number = position[1]  # comme "1", "2", "3"

    # Nous trouvons l'indice de la ligne et de la colonne.
    row_index = row_map[row_letter]
    col_index = col_map[col_number]

    # Trouvons à quel matrice cela appartient.
    board_row = row_index // 3
    board_col = col_index // 3

    # Trouvons la position dans la ligne et la colonne.
    sub_row_index = row_index % 3  # 0, 1, 2
    sub_col_index = col_index % 3  # 0, 1, 2

    # Nous assignons une valeur au matrice.
    board_de_jeu[board_row][board_col][sub_row_index][sub_col_index] = value

def regle1(current_player):
    global ancienne_pos, ancienne_save, game_still_on, b1, b2, b3, b4, b5, b6, b7, b8, b9, val
    print()
    print("------" + current_player + "'s turn! ------")

    pos2 = input("Veuillez entrer une position (ex: A1): [s pour enregistrer et quitter le mode de jeu]: ")

    if pos2 == "s":
        print("En Quittant le jeu . . .")
        ancienne_save = ancienne_pos[:]
        game_still_on = False
        return

    if pos2 not in val and pos2 != "save":
        print("ENTREZ UNE POSİTİON VALIDE! (ex: A5,B7:) ")
        regle1(current_player)
    elif pos2 in ancienne_pos:
        print("Cette place a été déjà jouée: ")
        regle1(current_player)
    elif pos2 in b1 and full_matrice(board1) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b2 and full_matrice(board2) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b3 and full_matrice(board3) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b4 and full_matrice(board4) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b5 and full_matrice(board5) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b6 and full_matrice(board6) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b7 and full_matrice(board7) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b8 and full_matrice(board8) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    elif pos2 in b9 and full_matrice(board9) == True:
        print("Jouez dans un place vide!!")
        regle1(current_player)
    else:
        update_board(pos2, current_player)
        ancienne_pos.append(pos2)

def get_input(current_player):
    print()
    print("------" + current_player + "'s turn! ------")

    global ancienne_pos,ancienne_save, game_still_on, haut_gauche, haut_centre, haut_droite, centre_gauche, centre_centre, centre_droite, bas_gauche, bas_centre, bas_droite, b1, b2, b3, b4, b5, b6, b7, b8, b9, val

    pos = input("Veuillez entrer une position (ex: A1): [s pour enregistrer et quitter le mode de jeu]: ")

    if pos == "s":
        print("En Quittant le jeu . . .")
        ancienne_save = ancienne_pos[:]
        game_still_on = False
        return

    if pos not in val:
        print("ENTREZ UN POSİTİON VALIDE! (ex: A5,B7: ")
        get_input(current_player)
        return
    elif pos in ancienne_pos:
        print("Cette place a été déjà jouée: ")
        get_input(current_player)
        return

    if len(ancienne_pos) >= 1:
        if pos not in val:
            print("ENTREZ UN POSİTİON VALIDE! (ex: A5,B7: ")
            get_input(current_player)
            return
        elif pos in ancienne_pos:
            print("Cette place a été déjà jouée: ")
            get_input(current_player)
            return

        elif ancienne_pos[-1] in haut_gauche and pos not in b1 and full_matrice(board1) == False:
            print("jouez dans la matrice en haut à gauche: ")
            get_input(current_player)
        elif ancienne_pos[-1] in haut_centre and pos not in b2 and full_matrice(board2) == False:
            print("jouez dans la matrice en haut au centre: ")
            get_input(current_player)
        elif ancienne_pos[-1] in haut_droite and pos not in b3 and full_matrice(board3) == False:
            print("jouez dans la matrice en haut à droite: ")
            get_input(current_player)
        elif ancienne_pos[-1] in centre_gauche and pos not in b4 and full_matrice(board4) == False:
            print("jouez dans la matrice au centre à gauche: ")
            get_input(current_player)
        elif ancienne_pos[-1] in centre_centre and pos not in b5 and full_matrice(board5) == False:
            print("jouez dans la matrice au centre: ")
            get_input(current_player)
        elif ancienne_pos[-1] in centre_droite and pos not in b6 and full_matrice(board6) == False:
            print("jouez dans la matrice au centre à droite: ")
            get_input(current_player)
        elif ancienne_pos[-1] in bas_gauche and pos not in b7 and full_matrice(board7) == False:
            print("jouez dans la matrice en bas à gauche: ")
            get_input(current_player)
        elif ancienne_pos[-1] in bas_centre and pos not in b8 and full_matrice(board8) == False:
            print("jouez dans la matrice en bas au centre: ")
            get_input(current_player)
        elif ancienne_pos[-1] in bas_droite and pos not in b9 and full_matrice(board9) == False:
            print("jouez dans la matrice en bas à droite: ")
            get_input(current_player)



        elif ancienne_pos[-1] in haut_gauche and pos in b1 and full_matrice(board1) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in haut_centre and pos in b2 and full_matrice(board2) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in haut_droite and pos in b3 and full_matrice(board3) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in centre_gauche and pos in b4 and full_matrice(board4) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in centre_centre and pos in b5 and full_matrice(board5) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in centre_droite and pos in b6 and full_matrice(board6) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in bas_gauche and pos in b7 and full_matrice(board7) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in bas_centre and pos in b8 and full_matrice(board8) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)
        elif ancienne_pos[-1] in bas_droite and pos in b9 and full_matrice(board9) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
            print(ancienne_pos)


        elif ancienne_pos[-1] in haut_gauche and full_matrice(
                board1) == True and pos in val and pos not in ancienne_pos and pos not in b1:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in haut_gauche and full_matrice(
                board1) == True and pos in val and pos not in ancienne_pos and pos in b1:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in haut_centre and full_matrice(
                board2) == True and pos in val and pos not in ancienne_pos and pos not in b2:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in haut_centre and full_matrice(
                board2) == True and pos in val and pos not in ancienne_pos and pos in b2:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in haut_droite and full_matrice(
                board3) == True and pos in val and pos not in ancienne_pos and pos not in b3:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in haut_droite and full_matrice(
                board3) == True and pos in val and pos not in ancienne_pos and pos in b3:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in centre_gauche and full_matrice(
                board4) == True and pos in val and pos not in ancienne_pos and pos not in b4:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in centre_gauche and full_matrice(
                board4) == True and pos in val and pos not in ancienne_pos and pos in b4:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in centre_centre and full_matrice(
                board5) == True and pos in val and pos not in ancienne_pos and pos not in b5:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in centre_centre and full_matrice(
                board5) == True and pos in val and pos not in ancienne_pos and pos in b5:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in centre_droite and full_matrice(
                board6) == True and pos in val and pos not in ancienne_pos and pos not in b6:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in centre_droite and full_matrice(
                board6) == True and pos in val and pos not in ancienne_pos and pos in b6:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in bas_gauche and full_matrice(
                board7) == True and pos in val and pos not in ancienne_pos and pos not in b7:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in bas_gauche and full_matrice(
                board7) == True and pos in val and pos not in ancienne_pos and pos in b7:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in bas_centre and full_matrice(
                board8) == True and pos in val and pos not in ancienne_pos and pos not in b8:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in bas_centre and full_matrice(
                board8) == True and pos in val and pos not in ancienne_pos and pos in b8:
            print("joue dans une matrice vide")
            get_input(current_player)
        elif ancienne_pos[-1] in bas_droite and full_matrice(
                board9) == True and pos in val and pos not in ancienne_pos and pos not in b9:
            print("vous pouvez jouer où vous voulez")
            update_board(pos, current_player)
            ancienne_pos.append(pos)
        elif ancienne_pos[-1] in bas_droite and full_matrice(
                board9) == True and pos in val and pos not in ancienne_pos and pos in b9:
            print("joue dans une matrice vide")
            get_input(current_player)

    else:
        print("")
        update_board(pos, current_player)
        ancienne_pos.append(pos)


def robot1(current_player):
    global ancienne_pos, pos3, b1, b2, b3, b4, b5, b6, b7, b8, b9, val
    if current_player == "X":
        robot = "O"
    else:
        robot = "X"

    print()
    print("------" + robot + "'s turn! ------")

    pos3 = robot_choice()

    if pos3 in ancienne_pos and ancienne_pos:
        robot1(current_player)
    elif pos3 in b1 and full_matrice(board1) == True:
        robot1(current_player)
    elif pos3 in b2 and full_matrice(board2) == True:
        robot1(current_player)
    elif pos3 in b3 and full_matrice(board3) == True:
        robot1(current_player)
    elif pos3 in b4 and full_matrice(board4) == True:
        robot1(current_player)
    elif pos3 in b5 and full_matrice(board5) == True:
        robot1(current_player)
    elif pos3 in b6 and full_matrice(board6) == True:
        robot1(current_player)
    elif pos3 in b7 and full_matrice(board7) == True:
        robot1(current_player)
    elif pos3 in b8 and full_matrice(board8) == True:
        robot1(current_player)
    elif pos3 in b9 and full_matrice(board9) == True:
        robot1(current_player)

    else:
        update_board(pos3, robot)
        ancienne_pos.append(pos3)

def get_input2_robot(current_player):
    global ancienne_pos, pos4, haut_gauche, haut_centre, haut_droite, centre_gauche, centre_centre, centre_droite, bas_gauche, bas_centre, bas_droite, b1, b2, b3, b4, b5, b6, b7, b8, b9, val
    if current_player == "X":
        robot = "O"
    else:
        robot = "X"

    pos4 = robot_choice()

    if len(ancienne_pos) >= 0:
        if pos4 in ancienne_pos:
            get_input2_robot(current_player)
            return

        elif ancienne_pos[-1] in haut_gauche and pos4 not in b1 and full_matrice(board1) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in haut_centre and pos4 not in b2 and full_matrice(board2) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in haut_droite and pos4 not in b3 and full_matrice(board3) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in centre_gauche and pos4 not in b4 and full_matrice(board4) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in centre_centre and pos4 not in b5 and full_matrice(board5) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in centre_droite and pos4 not in b6 and full_matrice(board6) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in bas_gauche and pos4 not in b7 and full_matrice(board7) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in bas_centre and pos4 not in b8 and full_matrice(board8) == False:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in bas_droite and pos4 not in b9 and full_matrice(board9) == False:
            get_input2_robot(current_player)

        elif ancienne_pos[-1] in haut_gauche and pos4 in b1 and full_matrice(board1) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in haut_centre and pos4 in b2 and full_matrice(board2) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in haut_droite and pos4 in b3 and full_matrice(board3) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in centre_gauche and pos4 in b4 and full_matrice(board4) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in centre_centre and pos4 in b5 and full_matrice(board5) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in centre_droite and pos4 in b6 and full_matrice(board6) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in bas_gauche and pos4 in b7 and full_matrice(board7) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in bas_centre and pos4 in b8 and full_matrice(board8) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)
        elif ancienne_pos[-1] in bas_droite and pos4 in b9 and full_matrice(board9) == False:
            print("Emplacement modifié avec succès.")
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
            print(ancienne_pos)

        elif ancienne_pos[-1] in haut_gauche and full_matrice(
                board1) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b1:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in haut_gauche and full_matrice(
                board1) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b1:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in haut_centre and full_matrice(
                board2) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b2:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in haut_centre and full_matrice(
                board2) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b2:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in haut_droite and full_matrice(
                board3) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b3:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in haut_droite and full_matrice(
                board3) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b3:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in centre_gauche and full_matrice(
                board4) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b4:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in centre_gauche and full_matrice(
                board4) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b4:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in centre_centre and full_matrice(
                board5) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b5:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in centre_centre and full_matrice(
                board5) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b5:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in centre_droite and full_matrice(
                board6) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b6:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in centre_droite and full_matrice(
                board6) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b6:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in bas_gauche and full_matrice(
                board7) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b7:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in bas_gauche and full_matrice(
                board7) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b7:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in bas_centre and full_matrice(
                board8) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b8:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in bas_centre and full_matrice(
                board8) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b8:
            get_input2_robot(current_player)
        elif ancienne_pos[-1] in bas_droite and full_matrice(
                board9) == True and pos4 in val and pos4 not in ancienne_pos and pos4 not in b9:
            update_board(pos4, robot)
            ancienne_pos.append(pos4)
        elif ancienne_pos[-1] in bas_droite and full_matrice(
                board9) == True and pos4 in val and pos4 not in ancienne_pos and pos4 in b9:
            get_input2_robot(current_player)

    else:
        print("")
        update_board(pos4, robot)
        ancienne_pos.append(pos4)


def decider_gagner_grille():
    global game_still_on, board1, board2, board3, board4, board5, board6, board7, board8, board9
    # PLACE CHERCHER POUR X
    if board1[0][0] == board1[0][1] == board1[0][2] == "X" or board1[1][0] == board1[1][1] == board1[1][2] == "X" or board1[2][0] == board1[2][1] == board1[2][2] == "X" or board1[0][0] == board1[1][0] == board1[2][0] == "X" or board1[0][1] == board1[1][1] == board1[2][1] == "X" or board1[0][2] == board1[1][2] == board1[2][2] == "X" or board1[0][0] == board1[1][1] == board1[2][2] == "X" or board1[0][2] == board1[1][1] == board1[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 1")
        update_board("A1", "x")
        update_board("A2", "x")
        update_board("A3", "x")
        update_board("B1", "x")
        update_board("B2", "x")
        update_board("B3", "x")
        update_board("C1", "x")
        update_board("C2", "x")
        update_board("C3", "x")
        printBoard()

    elif board2[0][0] == board2[0][1] == board2[0][2] == "X" or board2[1][0] == board2[1][1] == board2[1][2] == "X" or board2[2][0] == board2[2][1] == board2[2][2] == "X" or board2[0][0] == board2[1][0] == board2[2][0] == "X" or board2[0][1] == board2[1][1] == board2[2][1] == "X" or board2[0][2] == board2[1][2] == board2[2][2] == "X" or board2[0][0] == board2[1][1] == board2[2][2] == "X" or board2[0][2] == board2[1][1] == board2[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 2")
        update_board("A4", "x")
        update_board("A5", "x")
        update_board("A6", "x")
        update_board("B4", "x")
        update_board("B5", "x")
        update_board("B6", "x")
        update_board("C4", "x")
        update_board("C5", "x")
        update_board("C6", "x")
        printBoard()

    elif board3[0][0] == board3[0][1] == board3[0][2] == "X" or board3[1][0] == board3[1][1] == board3[1][2] == "X" or board3[2][0] == board3[2][1] == board3[2][2] == "X" or board3[0][0] == board3[1][0] == board3[2][0] == "X" or board3[0][1] == board3[1][1] == board3[2][1] == "X" or board3[0][2] == board3[1][2] == board3[2][2] == "X" or board3[0][0] == board3[1][1] == board3[2][2] == "X" or board3[0][2] == board3[1][1] == board3[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 3")
        update_board("A7", "x")
        update_board("A8", "x")
        update_board("A9", "x")
        update_board("B7", "x")
        update_board("B8", "x")
        update_board("B9", "x")
        update_board("C7", "x")
        update_board("C8", "x")
        update_board("C9", "x")
        printBoard()

    elif board4[0][0] == board4[0][1] == board4[0][2] == "X" or board4[1][0] == board4[1][1] == board4[1][2] == "X" or board4[2][0] == board4[2][1] == board4[2][2] == "X" or board4[0][0] == board4[1][0] == board4[2][0] == "X" or board4[0][1] == board4[1][1] == board4[2][1] == "X" or board4[0][2] == board4[1][2] == board4[2][2] == "X" or board4[0][0] == board4[1][1] == board4[2][2] == "X" or board4[0][2] == board4[1][1] == board4[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 4")
        update_board("D1", "x")
        update_board("D2", "x")
        update_board("D3", "x")
        update_board("E1", "x")
        update_board("E2", "x")
        update_board("E3", "x")
        update_board("F1", "x")
        update_board("F2", "x")
        update_board("F3", "x")
        printBoard()

    elif board5[0][0] == board5[0][1] == board5[0][2] == "X" or board5[1][0] == board5[1][1] == board5[1][2] == "X" or board5[2][0] == board5[2][1] == board5[2][2] == "X" or board5[0][0] == board5[1][0] == board5[2][0] == "X" or board5[0][1] == board5[1][1] == board5[2][1] == "X" or board5[0][2] == board5[1][2] == board5[2][2] == "X" or board5[0][0] == board5[1][1] == board5[2][2] == "X" or board5[0][2] == board5[1][1] == board5[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 5")
        update_board("D4", "x")
        update_board("D5", "x")
        update_board("D6", "x")
        update_board("E4", "x")
        update_board("E5", "x")
        update_board("E6", "x")
        update_board("F4", "x")
        update_board("F5", "x")
        update_board("F6", "x")
        printBoard()

    elif board6[0][0] == board6[0][1] == board6[0][2] == "X" or board6[1][0] == board6[1][1] == board6[1][2] == "X" or board6[2][0] == board6[2][1] == board6[2][2] == "X" or board6[0][0] == board6[1][0] == board6[2][0] == "X" or board6[0][1] == board6[1][1] == board6[2][1] == "X" or board6[0][2] == board6[1][2] == board6[2][2] == "X" or board6[0][0] == board6[1][1] == board6[2][2] == "X" or board6[0][2] == board6[1][1] == board6[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 6")
        update_board("D7", "x")
        update_board("D8", "x")
        update_board("D9", "x")
        update_board("E7", "x")
        update_board("E8", "x")
        update_board("E9", "x")
        update_board("F7", "x")
        update_board("F8", "x")
        update_board("F9", "x")
        printBoard()

    elif board7[0][0] == board7[0][1] == board7[0][2] == "X" or board7[1][0] == board7[1][1] == board7[1][2] == "X" or board7[2][0] == board7[2][1] == board7[2][2] == "X" or board7[0][0] == board7[1][0] == board7[2][0] == "X" or board7[0][1] == board7[1][1] == board7[2][1] == "X" or board7[0][2] == board7[1][2] == board7[2][2] == "X" or board7[0][0] == board7[1][1] == board7[2][2] == "X" or board7[0][2] == board7[1][1] == board7[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 7")
        update_board("G1", "x")
        update_board("G2", "x")
        update_board("G3", "x")
        update_board("H1", "x")
        update_board("H2", "x")
        update_board("H3", "x")
        update_board("I1", "x")
        update_board("I2", "x")
        update_board("I3", "x")
        printBoard()

    elif board8[0][0] == board8[0][1] == board8[0][2] == "X" or board8[1][0] == board8[1][1] == board8[1][2] == "X" or board8[2][0] == board8[2][1] == board8[2][2] == "X" or board8[0][0] == board8[1][0] == board8[2][0] == "X" or board8[0][1] == board8[1][1] == board8[2][1] == "X" or board8[0][2] == board8[1][2] == board8[2][2] == "X" or board8[0][0] == board8[1][1] == board8[2][2] == "X" or board8[0][2] == board8[1][1] == board8[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 8")
        update_board("G4", "x")
        update_board("G5", "x")
        update_board("G6", "x")
        update_board("H4", "x")
        update_board("H5", "x")
        update_board("H6", "x")
        update_board("I4", "x")
        update_board("I5", "x")
        update_board("I6", "x")
        printBoard()

    elif board9[0][0] == board9[0][1] == board9[0][2] == "X" or board9[1][0] == board9[1][1] == board9[1][2] == "X" or board9[2][0] == board9[2][1] == board9[2][2] == "X" or board9[0][0] == board9[1][0] == board9[2][0] == "X" or board9[0][1] == board9[1][1] == board9[2][1] == "X" or board9[0][2] == board9[1][2] == board9[2][2] == "X" or board9[0][0] == board9[1][1] == board9[2][2] == "X" or board9[0][2] == board9[1][1] == board9[2][0] == "X":
        print("Le joueur X, vous avez gagne en matrice 9")
        update_board("G7", "x")
        update_board("G8", "x")
        update_board("G9", "x")
        update_board("H7", "x")
        update_board("H8", "x")
        update_board("H9", "x")
        update_board("I7", "x")
        update_board("I8", "x")
        update_board("I9", "x")
        printBoard()

    # PLACE CHERCHER POUR O
    elif board1[0][0] == board1[0][1] == board1[0][2] == "O" or board1[1][0] == board1[1][1] == board1[1][2] == "O" or board1[2][0] == board1[2][1] == board1[2][2] == "O" or board1[0][0] == board1[1][0] == board1[2][0] == "O" or board1[0][1] == board1[1][1] == board1[2][1] == "O" or board1[0][2] == board1[1][2] == board1[2][2] == "O" or board1[0][0] == board1[1][1] == board1[2][2] == "O" or board1[0][2] == board1[1][1] == board1[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 1")
        update_board("A1", "o")
        update_board("A2", "o")
        update_board("A3", "o")
        update_board("B1", "o")
        update_board("B2", "o")
        update_board("B3", "o")
        update_board("C1", "o")
        update_board("C2", "o")
        update_board("C3", "o")
        printBoard()

    elif board2[0][0] == board2[0][1] == board2[0][2] == "O" or board2[1][0] == board2[1][1] == board2[1][2] == "O" or board2[2][0] == board2[2][1] == board2[2][2] == "O" or board2[0][0] == board2[1][0] == board2[2][0] == "O" or board2[0][1] == board2[1][1] == board2[2][1] == "O" or board2[0][2] == board2[1][2] == board2[2][2] == "O" or board2[0][0] == board2[1][1] == board2[2][2] == "O" or board2[0][2] == board2[1][1] == board2[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 2")
        update_board("A4", "o")
        update_board("A5", "o")
        update_board("A6", "o")
        update_board("B4", "o")
        update_board("B5", "o")
        update_board("B6", "o")
        update_board("C4", "o")
        update_board("C5", "o")
        update_board("C6", "o")
        printBoard()

    elif board3[0][0] == board3[0][1] == board3[0][2] == "O" or board3[1][0] == board3[1][1] == board3[1][2] == "O" or board3[2][0] == board3[2][1] == board3[2][2] == "O" or board3[0][0] == board3[1][0] == board3[2][0] == "O" or board3[0][1] == board3[1][1] == board3[2][1] == "O" or board3[0][2] == board3[1][2] == board3[2][2] == "O" or board3[0][0] == board3[1][1] == board3[2][2] == "O" or board3[0][2] == board3[1][1] == board3[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 3")
        update_board("A7", "o")
        update_board("A8", "o")
        update_board("A9", "o")
        update_board("B7", "o")
        update_board("B8", "o")
        update_board("B9", "o")
        update_board("C7", "o")
        update_board("C8", "o")
        update_board("C9", "o")
        printBoard()

    elif board4[0][0] == board4[0][1] == board4[0][2] == "O" or board4[1][0] == board4[1][1] == board4[1][2] == "O" or board4[2][0] == board4[2][1] == board4[2][2] == "O" or board4[0][0] == board4[1][0] == board4[2][0] == "O" or board4[0][1] == board4[1][1] == board4[2][1] == "O" or board4[0][2] == board4[1][2] == board4[2][2] == "O" or board4[0][0] == board4[1][1] == board4[2][2] == "O" or board4[0][2] == board4[1][1] == board4[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 4")
        update_board("D1", "o")
        update_board("D2", "o")
        update_board("D3", "o")
        update_board("E1", "o")
        update_board("E2", "o")
        update_board("E3", "o")
        update_board("F1", "o")
        update_board("F2", "o")
        update_board("F3", "o")
        printBoard()

    elif board5[0][0] == board5[0][1] == board5[0][2] == "O" or board5[1][0] == board5[1][1] == board5[1][2] == "O" or board5[2][0] == board5[2][1] == board5[2][2] == "O" or board5[0][0] == board5[1][0] == board5[2][0] == "O" or board5[0][1] == board5[1][1] == board5[2][1] == "O" or board5[0][2] == board5[1][2] == board5[2][2] == "O" or board5[0][0] == board5[1][1] == board5[2][2] == "O" or board5[0][2] == board5[1][1] == board5[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 5")
        update_board("D4", "o")
        update_board("D5", "o")
        update_board("D6", "o")
        update_board("E4", "o")
        update_board("E5", "o")
        update_board("E6", "o")
        update_board("F4", "o")
        update_board("F5", "o")
        update_board("F6", "o")
        printBoard()

    elif board6[0][0] == board6[0][1] == board6[0][2] == "O" or board6[1][0] == board6[1][1] == board6[1][2] == "O" or board6[2][0] == board6[2][1] == board6[2][2] == "O" or board6[0][0] == board6[1][0] == board6[2][0] == "O" or board6[0][1] == board6[1][1] == board6[2][1] == "O" or board6[0][2] == board6[1][2] == board6[2][2] == "O" or board6[0][0] == board6[1][1] == board6[2][2] == "O" or board6[0][2] == board6[1][1] == board6[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 6")
        update_board("D7", "o")
        update_board("D8", "o")
        update_board("D9", "o")
        update_board("E7", "o")
        update_board("E8", "o")
        update_board("E9", "o")
        update_board("F7", "o")
        update_board("F8", "o")
        update_board("F9", "o")
        printBoard()

    elif board7[0][0] == board7[0][1] == board7[0][2] == "O" or board7[1][0] == board7[1][1] == board7[1][2] == "O" or board7[2][0] == board7[2][1] == board7[2][2] == "O" or board7[0][0] == board7[1][0] == board7[2][0] == "O" or board7[0][1] == board7[1][1] == board7[2][1] == "O" or board7[0][2] == board7[1][2] == board7[2][2] == "O" or board7[0][0] == board7[1][1] == board7[2][2] == "O" or board7[0][2] == board7[1][1] == board7[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 7")
        update_board("G1", "o")
        update_board("G2", "o")
        update_board("G3", "o")
        update_board("H1", "o")
        update_board("H2", "o")
        update_board("H3", "o")
        update_board("I1", "o")
        update_board("I2", "o")
        update_board("I3", "o")
        printBoard()

    elif board8[0][0] == board8[0][1] == board8[0][2] == "O" or board8[1][0] == board8[1][1] == board8[1][2] == "O" or board8[2][0] == board8[2][1] == board8[2][2] == "O" or board8[0][0] == board8[1][0] == board8[2][0] == "O" or board8[0][1] == board8[1][1] == board8[2][1] == "O" or board8[0][2] == board8[1][2] == board8[2][2] == "O" or board8[0][0] == board8[1][1] == board8[2][2] == "O" or board8[0][2] == board8[1][1] == board8[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 8")
        update_board("G4", "o")
        update_board("G5", "o")
        update_board("G6", "o")
        update_board("H4", "o")
        update_board("H5", "o")
        update_board("H6", "o")
        update_board("I4", "o")
        update_board("I5", "o")
        update_board("I6", "o")
        printBoard()

    elif board9[0][0] == board9[0][1] == board9[0][2] == "O" or board9[1][0] == board9[1][1] == board9[1][2] == "O" or board9[2][0] == board9[2][1] == board9[2][2] == "O" or board9[0][0] == board9[1][0] == board9[2][0] == "O" or board9[0][1] == board9[1][1] == board9[2][1] == "O" or board9[0][2] == board9[1][2] == board9[2][2] == "O" or board9[0][0] == board9[1][1] == board9[2][2] == "O" or board9[0][2] == board9[1][1] == board9[2][0] == "O":
        print("Le joueur O, vous avez gagne en matrice 9")
        update_board("G7", "o")
        update_board("G8", "o")
        update_board("G9", "o")
        update_board("H7", "o")
        update_board("H8", "o")
        update_board("H9", "o")
        update_board("I7", "o")
        update_board("I8", "o")
        update_board("I9", "o")
        printBoard()


def decider_gagant_jeu():
    global game_still_on
    if board1 == board2 == board3 == [["x", "x", "x"], ["x", "x", "x"],["x", "x", "x"]] or board1 == board4 == board7 == [["x", "x", "x"],["x", "x", "x"], ["x", "x","x"]] or board3 == board6 == board9 == [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]] or board2 == board5 == board8 == [["x", "x", "x"],["x", "x", "x"], ["x", "x","x"]] or board4 == board5 == board6 == [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]] or board7 == board8 == board9 == [["x", "x", "x"],["x", "x", "x"], ["x", "x","x"]] or board1 == board5 == board9 == [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]] or board3 == board5 == board7 == [["x", "x", "x"],["x", "x", "x"],["x", "x", "x"]]:
        print("Le joueur X, Vous avez gagné, Félicitation")
        game_still_on = False
    elif board1 == board2 == board3 == [["o", "o", "o"], ["o", "o", "o"],["o", "o", "o"]] or board1 == board4 == board7 == [["o", "o", "o"],["o", "o", "o"], ["o", "o","o"]] or board3 == board6 == board9 == [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]] or board2 == board5 == board8 == [["o", "o", "o"],["o", "o", "o"], ["o", "o","o"]] or board4 == board5 == board6 == [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]] or board7 == board8 == board9 == [["o", "o", "o"],["o", "o", "o"], ["o", "o","o"]] or board1 == board5 == board9 == [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]] or board3 == board5 == board7 == [["o", "o", "o"],["o", "o", "o"],["o", "o", "o"]]:
        print("Le joueur O, Vous avez gagné, Félicitation")
        game_still_on = False


def decider_egalite():
    global game_still_on
    if full_matrice(board1) == full_matrice(board2) == full_matrice(board3) == full_matrice(board4) == full_matrice(board5) == full_matrice(board6) == full_matrice(board7) == full_matrice(board8) == full_matrice(board9) == True:
        print("Egalite dans le jeu: ")
        game_still_on = False


def switch_player():
    global current_player
    if current_player == "X":  # if the current player is X then switch to O
        current_player = "O"
    elif current_player == "O":  # if the current player is O then switch to X
        current_player = "X"


def full_matrice(matrice):
    for row in matrice:
        for elem in row:
            if elem not in {"X", "O", "x", "o"}:
                return False
    return True


def player():
    plays = input("Vous voulez X ou O: ")
    if plays == "X":
        current_player = "X"
    elif plays == "O":
        current_player = "O"
    else:
        return player()
    return current_player


def robot_choice():
    global val
    pos3 = random.choice(val)
    return pos3


def clear_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            matrice[i][j] = "_"


def clear_all_matrices():
    global board1, board2, board3, board4, board5, board6, board7, board8, board9
    clear_matrice(board1), clear_matrice(board2), clear_matrice(board3), clear_matrice(board4), clear_matrice(board5), clear_matrice(board6), clear_matrice(board7), clear_matrice(board8), clear_matrice(board9)


def play_game():  # function which run the game
    global current_player,ancienne_pos2,ancienne_pos
    current_player = player()
    printBoard()
    while game_still_on:
        get_input(current_player)
        decider_gagner_grille()
        decider_gagant_jeu()
        decider_egalite()
        printBoard()
        switch_player()
        ancienne_pos2 = ancienne_pos


def play_game2():
    global current_player,ancienne_pos2,ancienne_pos
    current_player = player()
    printBoard()
    while game_still_on:
        regle1(current_player)
        decider_gagner_grille()
        decider_gagant_jeu()
        decider_egalite()
        printBoard()
        switch_player()
        ancienne_pos2 = ancienne_pos


def play_game3():
    global current_player,ancienne_pos2,ancienne_pos
    current_player = player()
    printBoard()
    while game_still_on:
        regle1(current_player)
        decider_gagner_grille()
        decider_gagant_jeu()
        decider_egalite()
        printBoard()
        ancienne_pos2 = ancienne_pos
        if game_still_on:
            robot1(current_player)
            decider_gagner_grille()
            decider_gagant_jeu()
            decider_egalite()
            printBoard()
            ancienne_pos2 = ancienne_pos

def play_game4():
    global current_player,ancienne_pos2,ancienne_pos
    current_player = player()
    printBoard()
    while game_still_on:
        get_input(current_player)
        decider_gagner_grille()
        decider_gagant_jeu()
        decider_egalite()
        ancienne_pos2 = ancienne_pos
        if game_still_on:
            printBoard()
            get_input2_robot(current_player)
            decider_gagner_grille()
            decider_gagant_jeu()
            decider_egalite()
            printBoard()
            ancienne_pos2 = ancienne_pos

def poser():
    global game_still_on, ancienne_pos, ancienne_pos_save, old_games, current_player
    while True:
        mode = input(
            "Quel mode voulez vous jouez (multiplayer) ou (singleplayer) ou (dernier) pour dernier mode (saisir q pour quitter): ")
        reg = input(
            "Quel regle voulez vous tester 1)pour jouez librement 2)pour mode tactic 3)pour continuer dernier jeu (saisir q pour quitter): ")

        if mode == "q" or reg == "q":
            print("Le jeu se ferme . . . ")
            return False

        if mode == "dernier" and reg == "3":
            if old_games:
                last_game = old_games[-1]
                if last_game == "m2":
                    old_games.append("m2")
                    for i in ancienne_save:
                        update_board(i, current_player)
                        switch_player()
                    for i in range(9):
                        decider_gagner_grille()
                    decider_gagant_jeu()
                    decider_egalite()
                    ancienne_pos = ancienne_pos2
                    play_game()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "m1":
                    old_games.append("m2")
                    for i in ancienne_save:
                        update_board(i, current_player)
                        switch_player()
                    for i in range(9):
                        decider_gagner_grille()
                    decider_gagant_jeu()
                    decider_egalite()
                    ancienne_pos = ancienne_pos2
                    play_game2()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "s1":
                    old_games.append("s1")
                    for i in ancienne_save:
                        update_board(i, current_player)
                        switch_player()
                    for i in range(9):
                        decider_gagner_grille()
                    decider_gagant_jeu()
                    decider_egalite()
                    ancienne_pos = ancienne_pos2
                    play_game3()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "s2":
                    old_games.append("s2")
                    for i in ancienne_save:
                        update_board(i, current_player)
                        switch_player()
                    for i in range(9):
                        decider_gagner_grille()
                    decider_gagant_jeu()
                    decider_egalite()
                    ancienne_pos = ancienne_pos2
                    play_game4()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                else:
                    print("Aucun jeu précédent à continuer!")
            else:
                print("Aucun jeu précédent trouvé!")
            continue

        elif mode == "multiplayer" and reg == "1":
            old_games.append("m1")
            play_game2()
            game_still_on = True
            ancienne_pos = []
            clear_all_matrices()

        elif mode == "multiplayer" and reg == "2":
            old_games.append("m2")
            play_game()
            game_still_on = True
            ancienne_pos = []
            clear_all_matrices()

        elif mode == "singleplayer" and reg == "1":
            old_games.append("s1")
            play_game3()
            game_still_on = True
            ancienne_pos = []
            clear_all_matrices()

        elif mode == "singleplayer" and reg == "2":
            old_games.append("s2")
            play_game4()
            game_still_on = True
            ancienne_pos = []
            clear_all_matrices()

        elif mode == "dernier" and reg == "1":
            if old_games:
                last_game = old_games[-1]
                if last_game == "m2":
                    old_games.append("m1")
                    play_game2()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "m1":
                    old_games.append("m1")
                    play_game2()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "s1":
                    old_games.append("s1")
                    play_game3()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "s2":
                    old_games.append("s1")
                    play_game3()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
        elif mode == "dernier" and reg == "2":
            if old_games:
                last_game = old_games[-1]
                if last_game == "m2":
                    old_games.append("m2")
                    play_game()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "m1":
                    old_games.append("m2")
                    play_game()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "s1":
                    old_games.append("s2")
                    play_game4()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                elif last_game == "s2":
                    old_games.append("s2")
                    play_game4()
                    game_still_on = True
                    ancienne_pos = []
                    clear_all_matrices()
                else:
                    print("Aucun jeu précédent à continuer!")
            else:
                print("Aucun jeu précédent trouvé!")
            continue
        else:
            print("Choix invalide, veuillez réessayer.")


poser()
#programme principal
