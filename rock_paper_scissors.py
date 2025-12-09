import random


def get_choices():
    player_choice = input("\n\nEnter a choice (Rock Paper Scissors)\t")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


choices = get_choices()
print(choices)


def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}")

    if player == computer:
      return "It's a tie"
    elif player == "rock":
     if computer == "scissors":
      return "Rock Smashes Scissors, YOU WIN!!"
    elif player == "paper":
      return "Paper CoversRock Rock, YOU WIN!!"
    elif player == "scissors":
     if computer == "paper":
      return "Scissors slices paper, YOU WIN!!"
    else:
      return "You lose!"


result = check_win(choices["player"], choices["computer"])
print(result)

