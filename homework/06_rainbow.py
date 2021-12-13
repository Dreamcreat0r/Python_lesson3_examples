# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

'''
x_start = 50
y_start = 50
x_end = 350
y_end = 450
for color in rainbow_colors:
    point_start = sd.get_point(x_start, y_start)
    y_start += 5
    point_end = sd.get_point(x_end, y_end)
    y_end += 5
    sd.line(point_start, point_end, color = color, width = 4)
'''

radius = 500
point_round = sd.get_point(150, -200)
for color in rainbow_colors:
    radius += 30
    sd.circle(point_round, radius, color, 30)


sd.pause()