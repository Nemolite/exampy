n = int(input())
k = int(input())
piople = [(i) for i in range(1, n+1)]
while len(piople)>1:
    for i in range(1,k):
        temp = piople.pop(0)
        piople.append(temp)
    piople.pop(0)
print(piople[0])
