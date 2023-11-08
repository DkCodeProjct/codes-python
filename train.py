
def main():
    while True:
        getUserTime = input("enter_Time please: ##:## ")
        convertUserTime = convert(getUserTime)

        if 7.0 <= convertUserTime <= 8.0:
            print("let's eat ")
        
        elif 8.5 <=  convertUserTime <= 9.0:
            print("get shit if need, else Do work")
        
        elif  12.0 <=  convertUserTime <= 13.0:
            print("eat if need, else take some break and youtube!!")
        
        elif   13.15 <=  convertUserTime <= 15.0:
            print("eat or drink something if need, else take brak and go outSide")
        
        elif  16.0 <=  convertUserTime <= 18.0:
            print("finish all the work, if unfinished do or procastinate")
        
        elif 18.15 <= convertUserTime <= 19.45:
            print("get ready to read somthing, eat, drink, youtube and go to bed")
        
        elif convertUserTime >= 9.00:
            print("sleep if need, else_: watch Porn, do what you need ")
        
        else:
            print("invalid input")
        
        check = input("checkTheRoutinMore(y/n)").lower()
        if check == 'n':
            break
    print("Ok, good luck for the day!!")

def convert(time):
    hours, muinet = time.split(":")
    
    newHour = float(hours)
    newmuint = float(muinet)
    
    totalTime = newHour + newmuint / 60
    return totalTime

if __name__ == "__main__":
    main()


    

