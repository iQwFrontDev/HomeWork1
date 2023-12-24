#Задача #1


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
else:
    print('Фраза 2 длинее фразы 1')


#Задача №2


year = 2021
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный год')
else:
    print('Обычный год')


#Задача №3


day = int(input('Введите день: '))
mounth = input('Введите месяц: ')
zodiac = 'Ваш знак задиака: '
# if (day >= 23 and mounth =='Октябрь' or 'октябрь') or (day <= 21 and mounth == 'Ноябрь' or 'ноябрь'):
if (day >= 23 and mounth == 'Октябрь') or (day <= 21 and mounth == 'Ноябрь'):
    print (zodiac + 'Скорпион')
elif (day >= 23 and mounth == 'Сентябрь') or (day <= 22 and mounth == 'Октябрь'):
    print (zodiac + 'Весы')
elif (day >= 23 and mounth == 'Август') or (day <= 22 and mounth == 'Сентябрь'):
    print (zodiac + 'Дева')
elif (day >= 23 and mounth == 'Июль') or (day <= 22 and mounth == 'Август'):
    print (zodiac + 'Лев')
elif (day >= 21 and mounth == 'Июнь') or (day <= 22 and mounth == 'Июль'):
    print (zodiac + 'Рак')
elif (day >= 21 and mounth == 'Май') or (day <= 20 and mounth == 'Июнь'):
    print (zodiac + 'Близнецы')
elif (day >= 20 and mounth == 'Апрель') or (day <= 20 and mounth == 'Май'):
    print (zodiac + 'Телец')
elif (day >= 21 and mounth == 'Март') or (day <= 19 and mounth == 'Апрель'):
    print (zodiac + 'Овен')
elif (day >= 23 and mounth == 'Сентябрь') or (day <= 22 and mounth == 'Октябрь'):
    print (zodiac + 'Весы')
elif (day >= 22 and mounth == 'Ноябрь') or (day <= 21 and mounth == 'Декабрь'):
    print (zodiac + 'Стрелец')
elif (day >= 22 and mounth == 'Декабрь') or (day <= 19 and mounth == 'Январь'):
    print (zodiac + 'Козерог')
elif (day >= 20 and mounth == 'Январь') or (day <= 18 and mounth == 'Февраль'):
    print (zodiac + 'Водолей')
elif (day >= 19 and mounth == 'Февраль') or (day <= 20 and mounth == 'Март'):
    print (zodiac + 'Рыбы')


#Задача №4

width = 15
length = 15
height = 49

if (width <= 15 and length <= 15 and height <= 15):
    print('Коробка № 1')
elif (width >= 2000) or (length >= 2000) or (height >= 2000):
    print('Упаковка для лыж')
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    print('Коробка № 2')
else:
    print ('Коробка № 3')



