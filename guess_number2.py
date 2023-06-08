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
    while points > 0:
        print("\nYou have", points_player2, "points.")
        maximum_num = int(input("Player 2, guess the number: ")) # Telling player 2 to guess the number decided by player 1
        if maximum_num == secret_num: # If player's 2 number is the same as player's 1 number, print:
            print("That's right player 2, you are a genius!")
            break
        else:
            print("Incorrect number") # else print that it is not the number introduced by player 1
            points_player2 -= 10 # substract 10 points each time player 2 doesn't guees the number
            points -= 1
    if points_player2 > 0:
        print("You win with ", points_player2, "points") # Telling player 2 with how much points he/she win
    else:
        print("Player 1 wins!") # If not, player 1 is the winner 

guess_number_2()