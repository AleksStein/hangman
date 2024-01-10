mass = [5,4,3,2,1,6,8,7,10,9,13,12,11,15,14]

c1 = 0
l = len(mass)-1

while c1 < l:

    c2 = 0
    while c2 < l-c1:
        if mass[c2] > mass[c2+1]:
            mass[c2], mass[c2+1] = mass[c2+1], mass[c2]
        c2 += 1

    c1 += 1

print(mass)
print('111')
