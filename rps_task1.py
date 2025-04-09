import random
import time
print( " GAME NAME --> 🏆 ROCK-PAPER-SCISSOR 🏆\n INSTRUCTIONS: \n THERE ARE BASICALLY 3 CHOICES: \n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n RULE 1 : USER NEED TO CHOOSE ANY OF THE CHOICES. \n --> ROCK WINS AGAINST SCISSORS. \n --> SCISSORS WIN AGAINST PAPER. \n --> PAPER WINS AGAINST ROCK. \n RULE 2: WINNER WILL BE DECLARED IN EACH ROUND BASED ON THE CHOICES CHOOSEN BY THE USER AND BOT. \n RULE 3: USER CAN QUIT THE GAME ANYTIME AFTER THE PARTCULAR ROUND IS FINISHED.")
    # ENTER YOUR NAME
print("_________________________________________________________________________________________________________")
user_name = input("Enter your name: ")
if user_name != "":
    print(f"Hello, {user_name}")
    print("Let's Start!!")
else:
    user_name = "USER"

    # Game choices
game_choices = ["Rock", "Paper", "Scissors"]

    # CALCULATING SCORES
user_score = 0
bot_score = 0

while True:
    # ENTER YOUR GAME CHOICE HERE
     user_choice = input("Enter your choice (0: Rock, 1: Paper, 2: Scissors, 'k' to quit): ")
     if user_choice.lower() == 'k':
         # Code in order to quit the game
         print(f"Final Score - {user_name}: {user_score}, Bot: {bot_score}")
         if user_score > bot_score:
             print("----------YOU WIN THE GAME------------")
         elif user_score == bot_score:
             print("-------IT'S A DRAW MATCH--------")
         else:
             print("----------BOT WON THE MATCH------------")
         print(f"Thanks for playing, {user_name}!! It was great playing with you!")
         time.sleep(15)
         break
     if not user_choice.isdigit() or int(user_choice) not in [0, 1, 2]:
         print("Invalid choice! Please enter 0, 1, or 2.")
         continue

     user_choice = int(user_choice)
     bot_choice = random.randint(0, 2)
     print(f"\n{user_name}'s Choice: {game_choices[user_choice]}")
     print(f"Bot's Choice: {game_choices[bot_choice]}")
            # Game logic
     if user_choice == bot_choice:
        print("It's a Draw!")
     elif (user_choice == 0 and bot_choice == 2) or \
         (user_choice == 1 and bot_choice == 0) or \
         (user_choice == 2 and bot_choice == 1):
         print("You Win!")
         user_score += 1
     else:
         print("You Lose!")
         bot_score += 1
        # Display updated scores
     print(f"Score - {user_name}: {user_score}, Bot: {bot_score}\n")

     play_again = input("Do you want to play again? (y/n): ").lower()
     if play_again != 'y':
        print(f"\nFinal Score - {user_name}: {user_score}, Bot: {bot_score}")
        if user_score > bot_score:
            print("----------YOU WIN THE GAME------------")
        elif user_score == bot_score:
            print("-------IT'S A DRAW MATCH--------")
        else:
            print("----------BOT WON THE MATCH------------")
        print(f"Thanks for playing, {user_name}!! It was great playing with you!")
        time.sleep(5)
        break

