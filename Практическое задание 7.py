a = int(input('Первоначальное количество километров: '))
b = int(input('Желаемый результат: '))
km_per_day = a/100*10 #увеличение километров в день
day = 1
print('В', day, '-й день вы пробежали:',a)
while b > a:
    day= day+1
    #print('В {0} день вы пробежали: '.format(day), a)
    km_per_day = a / 100 * 10
    a = float(a + km_per_day)
    print('В', day, '-й день вы пробежали: ''{:.2f}'.format(a))
print('В', day, 'вы пробежали больше ', b)
