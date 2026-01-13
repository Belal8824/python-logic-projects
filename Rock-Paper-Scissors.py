import random

print('Welcome to rock, paper, scissors game:')
begin = input('Press (enter) to continue or type (help) for rules: ').strip().lower()

if begin == 'help':
    print('''\n⭐⭐⭐⭐⭐⭐ Rules ⭐⭐⭐⭐⭐⭐
1) You choose and the computer chooses
2) Rock crushes Scissors → Rock wins
3) Scissors cut Paper → Scissors win
4) Paper covers Rock → Paper wins\n''')
elif begin == '':
    pass
else:
    print('Invalid input. Please restart and choose from the options.')
choice = input('Enter your choice (rock, paper, scissors): ').lower()
coco = ['rock', 'paper', 'scissors']
if choice not in coco:
    print('Invalid choice. Please choose rock, paper, or scissors.')
computer = random.choice(coco)
print(f'The computer chose {computer}, and you chose {choice}.')
if choice == computer:
    print("It's a draw!")
elif (choice == 'rock' and computer == 'scissors') or (choice == 'paper' and computer == 'rock') or (choice == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("You lose!")
