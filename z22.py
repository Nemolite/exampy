# На вход программе подается число
#
# n. Напишите программу, которая создает и выводит построчно список, состоящий из
#
# n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
n = int(input())
list2 =[]
list1 = [i for i in range(1,n+1)]
for i in range(1,n+1):
    list2.append(list1)
for k in range(n):
    print(list2[k])

