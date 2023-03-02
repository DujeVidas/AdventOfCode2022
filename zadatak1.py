with open('data1.txt') as f:
    data = [i for i in f.read().strip().split('\n')]

#print(data)
maks = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > maks:
        maks = count

print(maks)