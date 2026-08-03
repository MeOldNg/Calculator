import sys

def symbol():
    global prenum, nextnum, total
    sym = input("Enter the symbol (+, -, *, /, to exit enter '=' ) : ")
    match sym:
        case "+":
            total  = prenum + nextnum
            output()
            maincontinue()
        case "-":
            total = prenum - nextnum
            output()
            maincontinue()
        case "*":
            total = prenum * nextnum
            output()
            maincontinue()
        case "/":
            if nextnum == 0:
                print("Cannot be divided by zero, math error. ")
                main()
            elif prenum == 0:
                total = 0
                output()
                maincontinue()
            else:
                total = prenum / nextnum
                output()
                maincontinue()
        case "=":
            sys.exit()
        case _:
            print("Please enter a symbol from the provided list. ")
            symbol()

def maincontinue():
    global total, nextnum, prenum
    nextnumfunc()
    prenum = total
    symbol()

def output():
    print("The total is ", total, ".")

def prenumfunc():
    global prenum
    while True:
        try:
            prenum = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Input Error. Please enter the number again. ")
    return prenum

def nextnumfunc():
    global nextnum
    while True:
        try:
            nextnum = float(input("Enter the next number: "))
            break
        except ValueError:
            print("Input Error. Please enter the number again. ")
    return nextnum

def main():
    global prenum, nextnum
    print("Basic Calculator")
    prenumfunc()
    nextnumfunc()
    symbol()

if __name__ == "__main__":
    main()
