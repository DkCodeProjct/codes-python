def main():
    getInput = input("enterPassword ")
    if isvalid(getInput):
        getName = input("enterName ")
        result = getName[::-1]
        print(f"password keyString // {result.capitalize()}kEy")
    else:
        print("invlaid")
def isvalid(n):
    if n[0].isdigit() == False and n[1].isdigit() == False:
        return False
    if len(n) < 2 and len(n) > 6:
        return False
    i = 0
    while i < len(n):
        if n[i].isdigit() == False:
            if n[i] == "@":
                return False
        i += 1

        for int in n:
            if int in [" ", "9", "0", ","]:
                return False
        return True
main()