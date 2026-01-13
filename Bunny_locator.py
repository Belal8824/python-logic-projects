h=[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
print(f'''
welcome to place the rabbit
{h[0]}
{h[1]}
{h[2]}
where should the rabbit go ?''')
n=input('please choose a row and column\n')
r=int(n[0])
c=int(n[1])
h[r-1][c-1]='🐇'
print(f'''{h[0]}
{h[1]}
{h[2]}''')
