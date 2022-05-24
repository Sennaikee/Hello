x = eval(input ('Enter how high: '))
y = eval(input ('Enter how wide: '))
for i in range (x):
    for j in range (y):
        if(i==0 or i== x - 1 or j == 0 or j == y-1):
            print('*', end = ' ' )
        else:
            print(' ',end=' ')
    print()
    
