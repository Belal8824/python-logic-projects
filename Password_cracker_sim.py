import random
import string

# المستخدم يدخل الباسورد مرة واحدة
real_password = input('Please enter the password: ')

# المستخدم يدخل التفاصيل مرة واحدة
password_length = int(input('Enter password length: '))
letters_count = int(input('How many letters: '))
numbers_count = int(input('How many numbers: '))
symbols_count = int(input('How many symbols: '))

# تأكد ان الإجمالي مطابق لطول الباسورد
if letters_count + numbers_count + symbols_count != password_length:
    print("Error: Total of letters, numbers, and symbols must equal password length!")
    exit()

attempts = 0
generated_password = ''

while generated_password != real_password:
    letters = random.choices(string.ascii_letters, k=letters_count)
    numbers = random.choices(string.digits, k=numbers_count)
    symbols = random.choices(string.punctuation, k=symbols_count)

    # دمجهم في لستة وحدة
    temp = letters + numbers + symbols
    random.shuffle(temp)

    generated_password = ''.join(temp)
    attempts += 1
    print(f'Attempt {attempts}: {generated_password}')

print(f'\nCorrect! The password is: {generated_password}')
print(f'Total attempts: {attempts}')
