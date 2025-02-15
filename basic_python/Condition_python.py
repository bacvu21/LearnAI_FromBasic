# num = 10
# if num > 0 : 
#     print("Positive Number")
# elif num == 0: 
#     print("Zero")
# else: 
#     print("negative Number")

###List 

# fruits = ["apple","banana", "cherry"]

# for fruit in fruits:
#     print("\n" + fruit +"\n")
    
# for fruit in range(3): 
#     print(fruits[fruit])


finalCalculate = 0


def sum(a, b): 
    return a+ b;
def subtract(a,b): 
    return a-b;
def multiple(a,b):
    return a*b;
def divide(a,b):
    return a/b;

while True:
    userInputFirst = int(input())
    userInputMask = str(input())
    userInputSeccond = int(input())

    if userInputMask == "+": 
        print("Total sum data: " + str(sum(userInputFirst,userInputSeccond )))
    elif userInputMask == "-":
        print("Subtract data: "  + str(subtract(userInputFirst,userInputSeccond )))
    elif userInputMask == "*":
        print("Multiple data: "  + str(multiple(userInputFirst,userInputSeccond )))
    elif userInputMask == "/":
        print("Divide data: "  + str(divide(userInputFirst,userInputSeccond )))
    else : 
        print("Invalid mask input")
        







