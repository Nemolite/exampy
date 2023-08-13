# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел.
# Напишите программу, которая меняет местами соседние элементы списка
# (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов,
# то последний остается на своем месте.

elements = list(map(int, input().split()))
el_len = len(elements) if len(elements)%2==0 else len(elements)-1
for i in range(0,el_len,2):
    temp = elements[i]
    elements[i] = elements[i+1]
    elements[i+1] = temp
print(" ".join(map(str,elements)))