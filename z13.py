songs = {
    'Bad Guy': 3,
    'Thunder': 3,
    'Sweater Weather': 4,
    'Numb': 3,
    'Karma Police': 4,
    'Enjoy the Silence': 4,
    'Obstacles': 3,
    'Crosses': 2,
    'Unnamed Feeling': 7
}
marker = True
while marker:
    n = int(input())
    if n<=len(songs):
        marker = False
    else:
        info = "Вы не правильно ввели количесвто песень. Должно быть меньше {total_songs}. Повторите ввод: ".format(total_songs=len(songs))
        print(info)
        marker = True

input_assoc_arr = [ input() for i in range(1,n+1)]
res = 0
for k in songs:
    for m in input_assoc_arr:
        if m==k:
            res+=songs[k]
print(res)




