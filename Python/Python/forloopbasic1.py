#1
for x in range(151):
    print(x)

#2
for y in range (0,1001,5):
    print(y)

#3
for i in range (101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 ==0:
        print("Coding")
    else:
        print(i)

#4
sum = 0
for t in range (500000):
    if t % 2 != 0:
        sum = sum + t
print(sum)

#5
for v in range(2018, 0,  -4):
    print(v)

#6
lowNum = 5
highNum = 24
mult = 3
for z in range(25):
    if z % mult == 0 and z < highNum and z > lowNum:
        print(z) 