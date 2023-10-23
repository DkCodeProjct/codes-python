def get_input(prompt):
    while True:
        try:
            user = int(input(prompt))
            if user % 2 == 0:
                return user
            else:
                print("input__/odd")
        except ValueError:
            print("EnterA_Neumaric_Value_Please:_")

user_input = get_input("Enter__a evenDigit:_ ")
add = user_input * 2 + 5
sub = add - 12
dev = sub / 2
mul = dev * 2

print(f"Value:_{mul}")
print("CalculateTheMath!")


    