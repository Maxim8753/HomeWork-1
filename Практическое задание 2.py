seconds = int(input('Введите секунды: '))
minutes = int(seconds/60)
hour = float(minutes/60)
result = 'Это {0} часов, {1} минут или {2} секунд'.format(hour,minutes,seconds)
print('Часов: ', hour, ' Минут: ',minutes, ' Секунд: ',seconds)
print(result)
hours = int(seconds/3600)

print(f'{hours:02}:{minutes:02}:{seconds:02}')

