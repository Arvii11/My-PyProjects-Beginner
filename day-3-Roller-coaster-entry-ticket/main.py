print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print('Can ride.')
  age = int(input('Enter your age? '))
  if age < 12:
    if input('Do you want a photo of your ride?Y or N: ') == 'Y'.lower():
      print('Pay $8.')
    else:
      print('Pay $5.')
  elif 12 <= age <= 18:
    if input('Do you want a photo of your ride?Y or N: ') == 'Y'.lower():
      print('Pay $10.')
    else:
      print('Pay $7.')
  else:
    if input('Do you want a photo of your ride?Y or N: ') == 'Y'.lower():
      print('Pay $15.')
    else:
      print('Pay $12.')
else:
  print("Can't ride.")