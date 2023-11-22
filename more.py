def main():
    getNum = input("enter")
    if getNum.isdigit():
        verifiedGetNum = int(getNum)
        if isEven(verifiedGetNum):
            addNum = add(verifiedGetNum)
            print(f"Calculation: {addNum}")
            if addNum < 5 and addNum < 10:
                subNum = sub(addNum)
                print(f"Calculation: {subNum}")
            else:
                mulNum = mul(addNum)
                print(f"Calculation: {mulNum}")
        else:
            print("invalidDigit>>>")
    else:
        print("invlaidInput")
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
def add(num0):
    num0 = num0 + 2
    return num0
def sub(num1):
    num1 = num1 - 2
    return num1
def mul(num2):
    num2 = num2 * 1
    return num2
if __name__ == "__main__":
    main()

