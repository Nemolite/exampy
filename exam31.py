# Тема 4
# «Дополнительные возможности отладки»
#
# Домашняя работа 3
#
# Задание
# Используя библиотеки matplotlib и numpy произвести построение 2D графика где значение переменной x и y варируются от 0 до 50.
# Добавить подписи к графику и вывести на экран
#
# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 50)
y = np.arange(0, 50)
plt.plot(x)
plt.plot(y)
plt.title("Построение графика функции")
plt.show()