while True:
    a = float(input('Введите первое число: '))
    s = input('Введите операцию: ')
    if s == 'q':
        break
    b = float(input('Введите второе число: '))

    if s == '+':
        print(a+b)
    elif s == '-':
        print(a-b)
    elif s == '*':
        print(a*b)
    elif s == '/':
        if b !=0:
            print(a/b)
        else:
            print("Деление на ноль!")