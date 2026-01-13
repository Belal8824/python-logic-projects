length=int(input('enter password length'))
letters=int(input('how many letters'))
numbers=int(input('how many numbers'))
symbols=int(input('how many symbols'))
hhh=[]
if length!=letters+numbers+symbols:
    print('are u crazy')
else:
    import random
    import string
    x=random.choices(string.ascii_letters,k=letters)
    y=random.choices(string.digits,k=numbers)
    z=random.choices(string.punctuation,k=symbols)
    hhh.extend(x+y+z)
    random.shuffle(hhh)
    print('generated password is'+''.join(hhh))
