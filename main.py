x = int(input('Write the number of your flat: '))
porch = (x-1)//36+1
floor = (x-1)%36//4+1
if x<=144:
    print('Your porch is', porch, 'and your floor is', floor)
else: print('This flat doesn\'t exist')
