import getpass  # We used gatpass, this function allows you to hide the user's input in the console.

def guess_number_2():
    minimum_num = int(input("Enter the minimum of your rank: ")) # The user is prompted to enter his or her minimum rank.
    maximum_num = int(input("Enter the maximum of your rank: ")) # The user is prompted to enter his or her maximum rank.
    secret_num = getpass.getpass("Player 1, decide a number in the rank: ")
    secret_num = int(secret_num) # Here will be saved the secret number introduced by player 1
    if secret_num < minimum_num or secret_num > maximum_num:
        print("The number decided is not inside the rank, try with another!") # If the number decided by player 1 is not in the rank, print
        return
    points_player2 = 100 # player 2 has 100 inicial points
    points = 10