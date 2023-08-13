n = int(input())
part1 = 0
part2 = 0
part3 = 0
part4 = 0
for i in range(1,n+1):
    x, y = map(int, input().split())
    if (x>0 and y>0):
        part1+=1
    if (x<0 and y>0):
        part2+=1
    if (x<0 and y<0):
        part3+=1
    if (x>0 and y<0):
        part4+=1
    if (x==0 or y==0):
        continue
print('Первая четверть:',part1)
print('Вторая четверть:',part2)
print('Третья четверть:',part3)
print('Четвертая четверть:',part4)

