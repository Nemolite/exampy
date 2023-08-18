# Есть файл «input.txt», который содержит текст
# (включая буквы, цифры и другие видимые символы.
# Пробельных символов в тексте нет).
# Напишите программу, которая подсчитывает количество каждого из символов,
# а далее записывает эти данные в файл «answer.txt» в формате «буква: количество».

# Пример:
#
# Cодержимое файла input.txt:
#
# Hello,world!
#
# Содержимое файла answer.txt
#
# H: 1
#
# e: 1
#
# l: 3
#
# o: 2
#
# w: 1
#
# r: 1
#
# d: 1
#
# !: 1

input_file = open('input.txt','r')
output_file = open('answer.txt','w')
str_input_file = input_file.read().rstrip()
list_input_file = list(str_input_file)
uniqe_input_file = list(set(str_input_file))
for i in uniqe_input_file:
    tmp = 0
    for k in list_input_file:
        if i == k:
            tmp+=1
    if i!=''or i!='\n':
        info = "{i}:{tmp}".format(i=i,tmp=tmp)
    output_file.write(info)
    output_file.write('\n')

input_file.close()
output_file.close()




