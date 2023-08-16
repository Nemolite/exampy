# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" соответствует выпадению Орла, а буква "Р" - выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
op = input()
s =  list(op.split("О"))
x = list(filter(None,s))
arr = []
for i in range(len(x)):
    arr.append(len(x[i]))
maxr = arr[0]
for k in range(1,len(arr)):
    if arr[k] > maxr:
        maxr = arr[k]
print(maxr)







