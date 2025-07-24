def tic_tac_board():
    for a in range(3):
        if a != 0:
            print("-----------")
        row = " " + " | ".join([" "]*3)
        print(row)
tic_tac_board()

# def print_tic_tac_toe_board():
#     board = [" " * 3 for _ in range(3)]
#     for i in range(3):
#         print(" " + " | ".join(board[i]))
#         if i < 2:
#             print("-----------")

# print_tic_tac_toe_board()

