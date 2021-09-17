chislo1 = int(input('Введите первое число: '))
operacia = input('Введите операцию (+, -, *, /, //, %, **): ')
chislo2 = int(input('Введите второе число: '))

if operacia == '+':
    print(chislo1 + chislo2)
elif operacia == '-':
    print(chislo1 - chislo2)
elif operacia == '*':
    print(chislo1 * chislo2)
elif operacia == '/':
    print(chislo1 / chislo2)
elif operacia == '//':
    print(chislo1 // chislo2)
elif operacia == '%':
    print(chislo1 % chislo2)
elif operacia == '**':
    print(chislo1 ** chislo2)
