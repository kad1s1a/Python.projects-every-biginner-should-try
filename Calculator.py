#crating a calculator simple code 
def Add ():
    x = input ("Enter number lowel ya wesmek: ")
    y = input ("Enter number thani : ")
    print(" the sum is :",float(x) + float(y))

def Sub ():
    x = input ("Enter number lowel ya wesmek: ")
    y = input ("Enter number thani : ")
    print(" the Substraction is :",float(x) - float(y))  

def Mul ():
    x = input ("Enter number lowel ya wesmek: ")
    y = input ("Enter number thani : ")
    print(" the Multiplication is :",float(x) * float(y))

def Dev ():
    x = input ("Enter number (nominator) lowel ya wesmek: ")
    y = input ("Enter number thani (denominator): ")
    if y==0:
        print("This value is forbidden ")
        Dev()
    else:
        result = float(x) / float(y)
        print(" the Devision is :",result)

def Pow ():
    x = input ("Enter your number : ")
    y = input ("Enter the power of your number: ")
    x = int(x)
    y = int(y)
    print(" the Power is :")
    i = 1
    result = 1                          # you can add the special cases such as when the base is equal to 0 or when the power is equal to 1 etc
    while i <= y :
        result = result*x 
        i+=1
    print(x,"to the power of", y , "is : ",int(result))

def Fac ():
    fact=1
    x = input ("Enter your number : ")  # you can add the special cases such as when x is equal to 0 or 1 and when the number is a negative number
    x = int(x)                          #always validate your numbers types
    for i in range (1,x+1):             # Why did i put x+1 ? because the "in range" does not reach till max number If x = 7 then i will reach 6 as a max so we add 1 to 1 
        fact= fact*i  
    print(" the Factorial is :",fact)
    
def DaUI():
    a = input ("******************************\n \n What operation you want to perform: \n \n 1 :Adding\n 2 :Substracting \n 3 :Deviding\n 4 :Multiplying\n 5 :Power\n 6 :Factorial \n 0 :Exit \n \n******************************************\nchoose a number from above\n")
    a = int(a)
    if a == 1:
        print("You are Adding, type your numbers you wish to add:")
        Add()
        DaUI()   # at the enf of each operation we recall the first UI function to do another operation
    elif a == 2:
        print("You are Substracting, type your numbers:")
        Sub()
        DaUI()

    elif a == 3:
        print("You are Deviding, type your numbers:")
        Mul()
        DaUI()
    elif a == 4:
        print("You are Multiplying, type your numbers:")
        Dev()
        DaUI()
    elif a == 5:
        print("You are performing a Power operation, type your numbers:")
        Pow()
        DaUI()
    elif a == 6:
        print   ("You are performing a Factorial operation, type your number:")
        Fac()
        DaUI()   
    elif a ==    0:
        print   ("Peace out !!")
        exit    
DaUI() # if you remove this line you will not have any results and the program won't give any operations to perform 