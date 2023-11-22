def main():
    getNum = int(input("input: "))
    if isValid(getNum):
        mul = getNum * 2
        add = mul + 2
        sub = add - 2
        if sub < 10:
            add1 = sub + 2
            if add1 > 2 or add1 < 16:
                dvide = add1 / 2
                if dvide < 4:
                    power = dvide ** 2
                    print(f"transform: {round(power)}")
                else:
                    print(f"transform: {round(dvide)}")
    else:
        print("ivnalid")

def isValid(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
            
        