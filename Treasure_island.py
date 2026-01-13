print('''

╱╱╱╱╱╱╱╱╱╭╮
╱╱╱╱╱╱╱╱╭╯╰╮
╭━━┳┳━┳━┻╮╭╋━━╮
┃╭╮┣┫╭┫╭╮┃┃┃┃━┫
┃╰╯┃┃┃┃╭╮┃╰┫┃━┫
┃╭━┻┻╯╰╯╰┻━┻━━╯
┃┃
╰╯
''')
a=input('''welcome to my island
there are two doors infront of you 🚪 a red door and 🚪 a blue door
which door do you want to open?\n''')
if a.lower()=='red':
  b=input('''
  great you intered the room
  you found three boxes: 🎁 white, 🎁 black, 🎁 green
  which box will you open?\n
  ''')
  if b.lower()=='white':
    print('oops! you opened a box full of snakes 🐍🐍🐍')
  elif b.lower()=='black':
    print('oops! you opened a box full of spiders 🕷️🕷️🕷️')
  elif b.lower()=='green':
    print('congradulations you founded the t̳r̳e̳a̳s̳u̳r̳e̳')
  else :
    print('invalid choice')
elif a.lower()=='blue':
  print(''' oops you choiced the crocodile door 🐊🐊🐊
  game over!''')
else:
  print('invalid choise')
