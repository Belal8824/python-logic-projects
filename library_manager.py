library=[]
book=input('Enter the name of a book you own: \n')
book_1=input('Enter the name of another book you own (or press "enter"to skip): \n')
library.append(book)
if book_1:
    library.append(book_1)
    A=input('Enter the name of another book you own (or press "enter"to skip): \n')
    if A :
        library.append(A)
        v=input('Enter the name of another book you own (or press "enter"to skip): \n')
        if v:
            library.append(v)
            print(f'your library is {library}')
        else:
            print(f'your library is {library}')
    else:
        print(f'your library:{library}')
else:
    print(f'your library:{library}')
wish_list=[]
d=input('Enter the name of a book you wish to have in the future: \n')
wish_list.append(d)
c=input('Enter the name of another book you wish to have (or press "enter" to skip): \n')
if c :
    wish_list.append(c)
    print(f'your wishlist: {wish_list}')
else :
    print(f'your wishlist: {wish_list}')
h=input("Enter the name of a book from your wishlist that you've acquired(or press 'enter' to skip): \n")
if h:
    library.append(h)
    wish_list.remove(h)
    print(f'''
Updated Library: {library}
Updated Wishlist: {wish_list}''')
else :
    print(f'''
Updated Library: {library}
Updated Wishlist: {wish_list}''')
k=input('Enter the name of a book from your library you wish to donate (or press "Enter" to skip): \n')
if k:
    library.remove(k)
    print(f'Final library after donations: {library}')
else:
    print(f'Final library after donations: {library}')
