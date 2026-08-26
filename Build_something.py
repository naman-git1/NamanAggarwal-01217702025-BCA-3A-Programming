from arts import word_list

from arts import stages
from arts import logo
print(logo)
import random
to_guess = random.choice(word_list)
empty_list = []
for letter in to_guess:
    empty_list += ["_"]
lives = 6
end_game = False

while not end_game:

    player_guess = input("Guess a letter to start the game \n").lower()

    for position in range(len(to_guess)):
        letter = to_guess[position]
        if player_guess == letter:
            empty_list[position] = letter

    print(empty_list)
    if player_guess not in to_guess:
        lives -= 1
        print(f"live left {lives}")
        if lives == 0 :
            end_game = True
            print("You lose!!")
            print(f"the word was {to_guess}")
    print(stages[lives])

    if "_" not in empty_list:
        end_game = True
        print("You win!!!!")
        print(f"the word was {to_guess}")


