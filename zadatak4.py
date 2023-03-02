with open('data4.txt') as f:
    data = [i for i in f.read().strip().split('\n')]


count = 0
for line in data:
    arr = line.split(',')
    prvi = arr[0].split('-')
    drugi = arr[1].split('-')
    
    if int(prvi[0]) >= int(drugi[0]) and int(prvi[1]) <= int(drugi[1]):
        count +=1
    elif int(drugi[0]) >= int(prvi[0]) and int(drugi[1]) <= int(prvi[1]):
        count +=1


print(count)