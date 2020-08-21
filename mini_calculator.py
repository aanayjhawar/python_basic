# i=0
#
# while 6<7:
#
#     num1=int(input("Enter num1: \t"))
#     num2=int(input("Enter num2: \t"))
#     math_operation=input("Enter operation between - add, multiply, divide, diff: \t")
#     if math_operation=="add":
#         print(num1+num2)
#     elif math_operation=="multiply":
#         print(num1*num2)
#     elif math_operation=="divide":
#         print(num1/num2)
#     elif math_operation=="diff":
#         print(num1-num2)
#
#     else:
#         print("Bye")
#         break
#
#         i+=1

i=0

while True:
    num1=int(input("Enter num1: \t"))
    num2=int(input("Enter num2: \t"))
    math_operation=input("Enter operation between - add, multiply, divide, diff:\t ")

    if math_operation=="add":
        print(num1+num2)

    elif  math_operation=="multiply":
        print(num1*num2)
    elif(math_operation=="diff"):
        print(num1 - num2)
    elif(math_operation=="divide"):
        print(num1/num2)

    else:
        print("bye-for now !")
        break


    i+= 1



print("Hello")
