import re
n = int(input())
input_assoc_arr = [ input() for i in range(1,n+1)]
keys =[]
for key in range(len(input_assoc_arr)):
    if []!= re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', input_assoc_arr[key]):
        keys.append(key+1)
print(" ".join(map(str,keys)))