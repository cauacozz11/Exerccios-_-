num1 = float(input("coloca um numero: "))
num2 = float(input("coloca outro numero: "))
num3 = float(input("outro dnv: "))

if num1 >= num2:
    if num2 >= num3:
        print("a ordem é",num1,num2,num3)
    else:
        print("a ordem é",num1,num3,num2)
elif num2 >= num1:
    if num1 >= num3:
        print("a ordem é",num2,num1,num3)
    else:
        print("a ordem é",num2,num3,num1) 
elif num3 >= num1:
    if num1 >= num2:
        print("a ordem é",num3,num1,num2)
    else:
        print("a ordem é",num3,num2,num1)                           