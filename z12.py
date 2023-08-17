abv = [chr(i) for i in range(1072, 1104)]
zap = 'запретил букву'
wrd = input()
part_word = wrd + ' '+ zap
for i in abv:
    if i in part_word:
        full_word = part_word + ' ' + i
        if ''!=part_word:
            print(full_word.replace('  ', ' '))
        part_word = full_word.replace(i, '').strip()



