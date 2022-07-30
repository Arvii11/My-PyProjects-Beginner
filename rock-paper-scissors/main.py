rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice == 0:
  print('User Choice:\n')
  print(rock)
elif user_choice == 1:
  print('User Choice:\n')
  print(paper)
else:
  print('User Choice:\n')
  print(scissors)

if computer_choice == 0:
  print('Computer Choice:\n')
  print(rock)
elif computer_choice == 1:
  print('Computer Choice:\n')
  print(paper)
else:
  print('Computer Choice:\n')
  print(scissors)

if user_choice >= 3 or user_choice < 0:
  print('You typed invalid number') 
elif user_choice == 0 and computer_choice == 2:
  print('User has won')
elif user_choice == 2 and computer_choice == 0:
  print("Computer has won")
elif user_choice > computer_choice:
  print('User has won')
elif user_choice < computer_choice:
  print('Computer has won')
else:
  print('Draw')
  
  