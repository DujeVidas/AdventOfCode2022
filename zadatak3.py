with open('data3.txt') as f:
    data = [i for i in f.read().strip().split('\n')]


s = 0
for line in data:
    comp1 = line[0:len(line)//2]
    comp2 = line[len(line)//2:]
    matching = set(comp1) & set(comp2)
    slovo = matching.pop()
    if slovo.isupper():
        br = ord(slovo)-38
    else:
        br = ord(slovo)-96
    s+=br

print(s)
