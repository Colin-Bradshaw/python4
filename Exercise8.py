def func():
    print('Hello World')


def func1(name):
    print('Hi, my name is', name)


def func3(x,y,z):
    if z:
        return x
    elif not z:
        return y


def func4(x,y):
    return x*y


def is_even(x):
    if x%2 ==0:
        return True
    return False


def arg1Greater(x,y):
    if x > y:
        return True
    return False


def sum(*args):
    sum = 0
    for item in args:
        sum += item
    return sum


def arbitraryEven(*args):
    lst = []
    for item in args:
        if int(item) % 2 == 0:
            lst.append(int(item))

    return lst


def uppercaseEven(text):
    # only alpha characters are considered. spaces , punctuation are skipped without indexing
    # index begins at 0
    isEven = True
    ret = ""
    for letter in text:
        if str.isalpha(letter):
            if isEven:
                ret += str.upper(letter)
                isEven = False
            else:
                ret += str.lower(letter)
                isEven = True
    return ret


def ifEven(x,y):
    if x%2 == 0 and y%2 == 0:
        return min([x,y])
    else:
        return max([x,y])


def sameLetter(txt1, txt2):
    # treats uppercase and lower case as same letter
    if str.upper(txt1)[0] == str.upper(txt2)[0]:
        return True
    return False


def distanceFrom7(x):
    distance = x -7
    return 7 + distance * -2


def capitol4th(txt):
    first = txt[0].upper()
    fourth = txt[3].upper()
    txt = first + txt[1:3] + fourth + txt[4:]
    return txt


func()
func1('Colin')
print(func3(1,2,True))
print(func3(1,2,False))
print(func4(5,6))
print(is_even(8))
print(is_even(9))
print(arg1Greater(7,6))
print(arg1Greater(6,7))
print(sum(5,6,7,8))
print(arbitraryEven(5,6,7,8,9))
print(uppercaseEven("I am the Walrus"))
print(uppercaseEven("IamtheWalrus"))
print(ifEven(8,10))
print(ifEven(8, 9))
print(sameLetter('seraph', "Sally"))
print(sameLetter('seraph', 'bob'))
print(distanceFrom7(10))
print(capitol4th('string'))