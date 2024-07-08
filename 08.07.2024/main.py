import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Welcome to Rock, paper, scissors.")
player_choice = int(input("Write 0 for rock, 1 for paper and 2 for scissors."))
if player_choice == 0:
    print(f"""You choose:
{rock} """)
elif player_choice == 1:
    print(f"""You choose:
{paper} """)
elif player_choice == 2:
    print(f"""You choose:
{scissors} """)

comp_choice = random.randint(0, 2)
if comp_choice == 0:
    print(f"""Computer chose:
{rock} """)
elif comp_choice == 1:
    print(f"""Computer chose:
{paper} """)
elif comp_choice == 2:
    print(f"""Computer chose:
{scissors} """)

if player_choice == comp_choice:
    print("It's a tie!")
elif player_choice == 0:
    if comp_choice == 2:
        print("You win!")
    else:
        print("Computer wins!")
elif player_choice == 1:
    if comp_choice == 0:
        print("You win!")
    else:
        print("Computer wins!")
elif player_choice == 2:
    if comp_choice == 1:
        print("You win!")
    else:
        print("Computer wins!")
