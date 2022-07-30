import random

from hangman_art import logo
print(logo)

from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
blank_space = []
lives = 6

for letter in chosen_word:
  blank_space.append('_')
print(blank_space)

while blank_space != chosen_word_list:
  guess = input('Guess a letter?\n').lower()
  if guess in blank_space:
    print(f'You have already entered this letter.')
  
  for position in range(len(chosen_word)):
    if chosen_word_list[position] == guess:
      blank_space[position] = guess
  if guess not in chosen_word_list:
    lives -= 1
      
  print(stages[lives])
  if lives == 0:
    print('Game Over.You lose!')
  print(f' '.join(blank_space))
print('Game Over.You win!')

  