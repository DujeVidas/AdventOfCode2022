with open('data2.txt') as f:
    data = [i for i in f.read().strip().split('\n')]

print(data)
s=0

dWin ={
    'X':'C',
    'Y':'A',
    'Z':'B'
}

"A B C"
"X Y Z"
dDraw ={
    'X':'A',
    'Y':'B',
    'Z':'C'
}
dPoints ={
    'X':1,
    'Y':2,
    'Z':3
}

for item in data:
    if dWin[item[-1]] == item[0]:
        s+=6+dPoints[item[-1]]
    elif dDraw[item[-1]] == item[0]:
        s+=3+dPoints[item[-1]]
    else:
        s+=dPoints[item[-1]]
print(s)