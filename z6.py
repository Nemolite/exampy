# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел.
# Напишите программу циклического сдвига элементов списка направо,
# когда последний элемент становится первым,
# а остальные сдвигаются на одну позицию вперед,
# в сторону увеличения индексов.
txts = list(map(str, input().split()))
txts.insert(0,txts[len(txts)-1])
del txts[len(txts)-1]
print(" ".join(map(str,txts)))