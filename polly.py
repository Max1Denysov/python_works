
def loop():
    x = int(input('Enter the number: '))
    i = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            i += 1
            b = str(i)
            print('[', b, ']: ', x)
        elif x % 2 != 0:
            x = (x*3) + 1
            i += 1
            b = str(i)
            print('[', b, ']: ', x)

    print('Again ?')
    again = input('> ')
    if again == 'y':
        loop()

loop()


