#Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
def multThree():
    for i in range(-9, -300, -3):
        if i % -3 == 0:
            print(i)
multThree()

#Print integers from 2000 to 5280, using a WHILE.
def printWhile():
    i = 2000
    while i > 1999 and i < 5281:
        print(i)
        i += 1
printWhile()

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
def printInt():
    for i in range(1, 101, 1):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:    
            print(i)
printInt()

def flexCount():
    lowNum = 2
    highNum = 9
    mult = 3
    for i in range(highNum, lowNum, -1):
            if i % mult == 0:
                print(i)
flexCount()

def duplicates(arrayInput):
    newArr = [arrayInput[0]]
    for i in range(1, len(arrayInput)):
        if arrayInput[i] not in newArr:
            newArr.append(arrayInput[i])
    return newArr

print(duplicates([2,5,6,7,8,9,9,9,9,21,4,5,2]))