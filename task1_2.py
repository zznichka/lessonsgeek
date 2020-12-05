total_time = int( input('введите секунды   '))
hour = total_time // 3600
sec = total_time % 60
min = total_time % 3600 // 60

if hour < 10 :
    print(f'0{hour}', end=':')
else:
    print(hour, end=':')

if min < 10 :
    print(f'0{min}', end=':')
else:
    print(min, end=':')
if sec < 10 :
    print(f'0{sec}')
else:
    print(sec)

