user_digit = int(input('Введите число: '))


while user_digit < 0:
    print('введите положительное число ')
    user_digit = int(input('Введите число: '))

if user_digit >= 0:
    user_digit = str(user_digit)
    print(max(user_digit))




