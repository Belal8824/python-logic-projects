import string
send_massage= input('enter a massage\n')
send_shift_number=int(input('enter a shift number\n'))
def encrypt(message,shift):
  alphabet=string.ascii_lowercase
  encrypted_massege=''
  for letter in send_massage:
      if letter in alphabet:
        original_position=alphabet.index(letter)
        new_position=(original_position+send_shift_number)%26
        encrypted_massege+=alphabet[new_position]
      elif letter in string.ascii_uppercase:
        letter=letter.lower()
        original_position=alphabet.index(letter)
        new_position=(original_position+send_shift_number)%26
        encrypted_massege+=alphabet[new_position].upper()
      else:
        encrypted_massege+=letter
  print(encrypted_massege)
encrypt(send_massage,send_shift_number)
print('to get the original one just enter the shift number with negative sign\n')
solve=input('to begin press enter ')
if solve=='':
  send_massage= input('enter the massage\n')
  send_shift_number=int(input('enter a negative shift number\n'))
  encrypt(send_massage,send_shift_number)
else:
  print('goodbye')
