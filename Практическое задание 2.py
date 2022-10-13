seconds = int(input('Введите секунды: '))
minutes = int(seconds/60)
hours = int(seconds/3600)

print(f'{hours:02}:{minutes:02}:{seconds:02}')
#print('{:.0f}:{:.0f}:{:.0f}'.format(hours,minutes,seconds))

