# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

'''
point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position = point, radius = radius, width = 3)
'''

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

'''
def bubble(point, step):
    radius = 50
    point = sd.get_point(point[0], point[1])
    for _ in range(2):
        radius += step
        sd.circle(center_position = point, radius = radius)

bubble(point = (200, 200), step = 20)
'''

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

def bubble_row(start_point, center_step, radius):
    xaxis = start_point[0]
    yaxis = start_point[1]
    for _ in range(10):
        xaxis += center_step[0]
        yaxis += center_step[1]
        point = sd.get_point(xaxis, yaxis)
        sd.circle(center_position = point, radius = radius)


# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

'''
delta = 1
for _ in range(3):
    delta += 1 
    bubble_row((200, 100*delta), (30, 0), 20)
'''

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for _ in range(100):
    point = sd.random_point()
    sd.circle(center_position = point, radius = 20, width = 2)

sd.pause()


