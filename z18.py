N = int(input())
summa = 0
for num in range(2,N,2):
    if num%4 == 0:
        summa+=num
print(summa)