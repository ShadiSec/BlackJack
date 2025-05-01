import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Dictionary of cards. [Key = Face of card] : [Value = Value of the card].
cards = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# Generate the player hand
def player_hand():
    """
    Generates 2 cards for the player hand and separates them into
    their respective lists.
    """
    face_list = [] # Empty list.
    face = "" # Empty string.
    value = [] # Empty list.
    for i in range(2):
        temp_list = (random.choice(list(cards.items()))) # Converts dictionary items into a list of tuples.
        for item in temp_list: # Runs for every item in the tuple list.
            if isinstance(item, str): # Checks if the current item in the iteration is a str.
                face_list.append(item) # Adds the str to the 'face_list' list.
            elif isinstance(item, int): # Checks if the current item in the iteration is an int.
                value.append(item) # Adds the int to the 'value' list
    face += ", ".join(face_list) # Separates the list items by a ', ' then adds it to the string 'face'.
    return face, value, face_list # The function returns the face string and the cards' value.

def computer_hand():
    """
    Generates 2 random cards for the computer hand
    and splits them into their respective list.
    """
    face_list = [] # Empty list to store the face of the 2 randomly generated cards.
    face = "" # Empty string to concatenate the items in the face_list into a string.
    value = [] # Empty list to store the value of the 2 randomly generated cards.
    for i in range(2): # Grabs 2 random cards from the cards dictionary.
        temp_list = random.choice(list(cards.items())) # Creates a tuple list out of the selected pair.
        for item in temp_list: # Iterates for each item in the list.
            if isinstance(item, str): # Checks if the current item in the iteration is a str.
                face_list.append(item) # If it is, then add to the face_list. Because the faces of cards are stored as strings.
            elif isinstance(item, int): # Checks if the current item in the iteration is an int.
                value.append(item) # If so, then it adds the item to the value list. Because the values are stored as integers.
    face += ", ".join(face_list) # Updates the 'face' string by concatenating the face_list strings into a single str.
    return face, value, face_list # The function returns the str of faces, the value of those cards as a list, and the faces as a list.

def new_card(face_list, value_list):
    """
    Takes a cards face list and a cards value list
    and adds a card to them. A face to the face_list and a value
    to the value_list.
    """
    card = random.choice(list(cards.items())) # Selects a random pair from the dictionary and saves it to the card as a tuple list.
    for item in card: # Iterates for each item in the card list.
        if isinstance(item, int): # Checks if the item is an int.
            value_list.append(item) # If so, then add the item to the value_list provided.
        elif isinstance(item, str): # Check if the item in the generated card pair is a str.
            face_list.append(item) # If so, then add the item to the face_list provided.
    return ", ".join(face_list), face_list, value_list # Returns a concatenation of the face_list into a string, the list of faces, and the list of values.

def adjust_ace(face_list, value_list):
    while sum(value_list) > 21 and 11 in value_list:  # Checks for 'A' in the computer hand.
        ace_index = face_list.index("A")  # Finds the index of the 'A' card in the comp hand.
        if value_list[ace_index] == 11:  # Checks if the 'A' is equal to 11.
            value_list[ace_index] = 1  # If it is, then it sets it to 1.
    return sum(value_list)  # Re-calculates the sum of the total computer hand value.

play = True

print(logo)
player_face, player_value, face_list = player_hand()  # Generates the player card face and values then assigns them to their respective variable.
comp_face, comp_value, comp_face_list = computer_hand() # Generates the computer cards face and values and assigns them to their respective variables.

play_game = input("Would you like to play a game of BlackJack? Type 'y' or 'n': ").lower()

# If player does not want to play, exit the game.
if play_game == "n":
    play = False
    print("Come back when you're not a loser!!!")

# If player decided to play the game.
elif play_game == "y":
    player_total_value = sum(player_value)  # Calculates the total value of the Player's cards.
    comp_total_value = sum(comp_value)  # Calculates the total value of the Computer's cards.

    while play: # Keep the loop going as long as the variable 'play' is set to 'True'

        # Gets the new player_total_value after ace adjustment.
        player_total_value = adjust_ace(face_list=player_face, value_list=player_value)

        if (sorted(player_value) == [10, 11]) or (sorted(comp_value) == [10, 11]): # If player or computer have an A and 10 in their hand.
            if sorted(comp_value) == [10, 11]: # If the computer has an A and 10 in their hand, the computer wins.
                print(f"Your Hand: [{player_face}] | Value: {player_total_value}")  # Prints Player stats.
                print(f"Computer's First Card: [{comp_face}] | Value: {comp_total_value}")  # Prints Computer stats
                print("-" * 64)
                print("The computer has BlackJack.")
                print("You Lose!")
                play = False
            elif sorted(player_value) == [10, 11]: # If the player has an A and 10 in their hand, the player wins.
                print(f"Your Hand: [{player_face}] | Value: {player_total_value}")  # Prints Player stats.
                print(f"Computer's First Card: [{comp_face}] | Value: {comp_total_value}")  # Prints Computer stats
                print("-" * 64)
                print("You have BlackJack!")
                print("You Win!")
                play = False
            elif sorted(player_value) == sorted(comp_value):
                print(f"Your Hand: [{player_face}] | Value: {player_total_value}")  # Prints Player stats.
                print(f"Computer's First Card: [{comp_face}] | Value: {comp_total_value}")  # Prints Computer stats
                print("-" * 64)
                print("You both have BlackJack!")
                print("It's a Draw!")
        elif player_total_value > 21: # If player score is still over 21 after A is equal to 1, player loses.
            print(f"Your Hand: [{player_face}] | Value: {player_total_value}")  # Prints Player stats.
            print(f"Computer's First Card: [{comp_face_list[0]}] | Value: {comp_value[0]}")  # Prints Computer stats
            print("-" * 64)
            print("Your hand value is more than 21.")
            print("You Lose!")
            play = False
        else:
            print(f"Your Hand: [{player_face}] | Value: {player_total_value}")  # Prints Player stats.
            print(f"Computer's First Card: [{comp_face_list[0]}] | Value: {comp_value[0]}")  # Prints Computer stats

            hit_or_stand = input("Type 'y' to Hit or 'n' to Stand: ").lower() # Ask use if they'd like to get another card.

            if hit_or_stand == "y":
                player_face, face_list, player_value = new_card(face_list, player_value) # Draws new card.
            elif hit_or_stand == "n":
                while comp_total_value < 17: # When player stands. The computer will draw a card until they have a min value of 17.
                    new_card(comp_face_list, comp_value) # Draws a new card for the computer hand.
                    comp_face = ", ".join(comp_face_list) # Updates the face string with the newly added card.
                    comp_total_value = sum(comp_value) # Updates the new computer total value.

                print(f"Your Hand: [{player_face}] | Value: {player_total_value}")  # Prints Player stats.
                print(f"Computer's Hand: [{comp_face}] | Value: {comp_total_value}")  # Prints Computer stats

                # Gets the new comp_total_value after ace adjustment.
                comp_total_value = adjust_ace(face_list=comp_face_list, value_list=comp_value)

                if comp_total_value < player_total_value or comp_total_value > 21: # If the computer value is less than the player value OR the computer value is greater than 21. Player wins.
                    print("-" * 64)
                    print("You Win!")
                    play = False
                elif comp_total_value == player_total_value: # If player value is equal to computer value. It's a draw.
                    print("-" * 64)
                    print("It's a Draw!")
                    play = False
                else:
                    print("-" * 64)
                    print("You Lose!")
                    play = False
            else:
                print("Invalid Input")