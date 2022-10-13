user_cost = int(input('Введите издержку: '))
user_revenue = int(input('Введите выручку: '))

if user_revenue > user_cost:
    profit = user_revenue - user_cost
    print('Ваша прибыль составляет: ', profit)
elif user_revenue < user_cost:
    loss = user_cost - user_revenue
    print( 'Ваш убыток составляет: ', loss)
else:
    print('Вы вышли в 0 ')
