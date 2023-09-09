n = int(input('n='))
k= int(input('k='))
i=1
sp = []
while i<= n:
    sp.append(i)
    i += 1
print(sp)

while len(sp)>1:
    i= 1
    while i<k:
        temp = sp.pop(0)
        sp.append(temp)
        i=+1
sp.pop(0)

print(sp)


