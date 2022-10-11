for i in range (45, 210):

    if i == 100: continue

    if i == 205: break
    
    print(i)


sol = 7*24
guess = ''

while guess != sol:
    guess = int(input("what is the product of 7 * 24 ?"))
    print('Wrong')
else:
    print('You good in math')