user_cost = int(input('Введите издержку: '))
user_revenue = int(input('Введите выручку: '))
#user_workers = int(input('Введите количество человек на фирме: '))

if user_revenue > user_cost:
    profit = user_revenue - user_cost
    profitability = profit/user_revenue*100
    user_workers = int(input('Введите количество человек на фирме: '))
    profit_man = profit/user_workers
    print('Ваша прибыль составляет: ', profit)
    print('Ваша рентабельность: ', profitability)
    print('Прибыль на одного работника составляет: ', profit_man)
elif user_revenue < user_cost:
    loss = user_cost - user_revenue
    print('Ваш убыток составляет: ', loss)
else:
    print('Вы вышли в 0 ')
