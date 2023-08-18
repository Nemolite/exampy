# Напишите функцию, которая принимает на вход строку и возвращает количество гласных букв в строке.
# В строке используются только латинские символы.
# Регистр букв может быть любой.
#
# Пример входных данных 1:
# hello
# Пример выходных данных 1:
# 2
# Пример входных данных 2:
# Orange
# Пример выходных данных 2:
# 3
# В качестве ответа пришли только код функции.
def count_glas(in_str):
    str_gl = 'AEIOU'
    str_gl = str_gl + str_gl.lower()
    list_gl = list(str_gl)
    list_in = list(in_str)
    counter = 0
    for i in list_in:
        if i in list_gl:
            counter+=1
    return counter
in_str = input()
print(count_glas(in_str))
