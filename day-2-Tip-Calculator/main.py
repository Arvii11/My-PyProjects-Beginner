#Data Types
print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
tip = int(input('What is the prercentage tip you like to give? 10, 12, or 15? '))
split = int(input('How many people to split the bill? '))
final_amount = (total_bill * (tip/100)) + total_bill 
pay = final_amount/split
print('Each person should pay: ${0:0.2f}'.format(pay))