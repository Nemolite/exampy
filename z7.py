# На вход программе подается строка текста,
# содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел.
# Напишите программу для подсчета количества разных элементов в списке.
numbers = list(map(int, input().split()))
result = []
result.append(numbers[0])
for i in range(1,len(numbers)):
    if numbers[i] not in result:
        result.append(numbers[i])
print(len(result))