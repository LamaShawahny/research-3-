import os

# I used a text file to save the numbers and their results after applying the function "f"
# return x returns x which is the parameter of the number before "=" and the x that we send it to the function
def returnx(str):
    num = ""
    for ch in str:
        if ch == "=":
            break
        num = num + ch
    return int(num)
# it returns the value that we get when we call the function with x
def getVal(str):
    count = 0
    Val = ""
    for ch in str:
        if ch == "=":
            break
        count = count + 1
    count = count + 1
    while count < len(str):
        Val = Val + str[count]
        count = count + 1
    return int(Val)

# The function
def f(x):
    return x ** 2

# it checks if we already have result or value for x or not
def Calc(x: int):
    if not os.path.exists('data.txt'):
        file = open("data.txt", "x")
    with open('data.txt') as fp:
        line = fp.readline()
        while line:
            if line.count("=") == 1:
                if x == returnx(line):
                    print("I already told you that the answer is " + str(getVal(line.replace("\n", ""))) + "!")
                    return
            line = fp.readline()

    res = f(x)
    lx = open("data.txt", "a")
    lx.write(str(x) + "=" + str(res) + '\n')
    lx.close()
    print("return " + str(res))


if __name__ == '__main__':
    Calc(2)
    Calc(3)
    Calc(3)