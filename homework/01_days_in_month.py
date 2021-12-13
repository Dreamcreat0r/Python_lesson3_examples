# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Enter month number please: ")
month = int(user_input)
print('You entered: ', month)

# TODO здесь ваш код
if month == 1:
    print('The first month is January, 31 day')
elif month == 2:
    print('The second month is February, 28 days')
elif month == 3:
    print('The third month is March, 31 day')
elif month == 4:
    print('The fourth month is April, 30 days')
elif month == 5:
    print('The fifth month is May, 31 day')
elif month == 6:
    print('The sixth month is June, 30 days')
elif month == 7:
    print('The seventh month is July, 31 day')
elif month == 8:
    print('The eighth month is August, 31 day')
elif month == 9:
    print('The nineth month is September, 30 days')
elif month == 10:
    print('The tenth month is October, 31 day')
elif month == 11:
    print('The eleventh month is November, 30 days')
elif month == 12:
    print('The twelvth month is December, 31 day')
