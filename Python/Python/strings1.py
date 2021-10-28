#remove blanks w/ built-in
def remove(stringSentence):
    return stringSentence.replace(" ", "")
print(remove("Test Test Test"))


#remove blanks w/o built-in
def remove2(stringSentence):
    newString = ""
    for i in range(len(stringSentence)):
        if stringSentence[i] != " ":
            newString+=stringSentence[i]
    return newString
print(remove2("Test Test Test"))


#return int w/ built-in
def returnInt(stringSentence):
    return int(filter(str.isdigit, stringSentence))
print(returnInt("ojfoiajsdf1odfoerwf8qokwenfokwenf2"))

#return int w/o built-in
def returnInt2(stringSentence):
    num = 0
    stringSentence.split()
    for i in range(len(stringSentence)):
        if type(stringSentence[i]) is int:
            num = num + stringSentence[i]
    return num


print(returnInt2("ojfoiajsdf1odfoerwf8qokwenfokwenf2"))


#return first character of word
def returnFirst(stringSentence):
    words = stringSentence.split()
    letters = [word[0] for word in words]
    return "".join(letters)
print(returnFirst("My name is Kevin"))

#Mapping
arr1 = ["abc",3,"yo"]
arr2 = [42, "wassup", True]

def mapping():
    mapping = dict(zip(arr1, arr2))
    return(mapping)

print(mapping())

#Invert Hash
def invert():
    dict1 = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
    inv_dict = {v: k for k, v in dict1.items()}
    return inv_dict
print(invert())



