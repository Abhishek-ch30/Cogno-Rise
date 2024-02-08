#This function adds two number
def add(num1,num2):
    return num1+num2
#This function substracts two number
def substract(num1,num2):
    return  num1-num2
#This function multiply two number
def multiply(num1,num2):
    return num1*num2
#This function divides two number
def division(num1,num2):
#Check if num2 is not zero to avoid division by zero error
    if num2!=0:
        return num1/num2
    else:
        print("ERROR!!!!Zero division error")
#This function raises num2 as a power of num1
def exponent(num1,num2):
    return num1**num2
def calculator():
    #displays the operation menu
    print("SELECT OPERATION")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Exit")
    #Enters in the calculator loop
    while True:
        select_operation=input("ENTER YOUR OPERATION:")
#check if the selected operation is in the above options
        if select_operation in  ('1', '2', '3', '4', '5'):
            try:
              #get numeric value from the user
                num1 = float(input("ENTER FIRST NUMBER: "))
                num2 = float(input("ENTER SECOND NUMBER: "))
            except ValueError:
                # Handles the case where the user enters non-numeric values
                print("INVALID INPUT!!!Enter correct number")
                continue
           # Check if the user chose to exit
        if select_operation == '6':
                print("Exiting the calculator. Goodbye!")
                break

        elif select_operation=='1':
                print(num1,"+",num2,"=",add(num1,num2))
        elif select_operation=='2':
                print(num1,"-",num2,"=",substract(num1,num2))
        elif select_operation=='3':
                print(num1,"*",num2,"=",multiply(num1,num2))
        elif select_operation=='4':
                print(num1,"/",num2,"=",division(num1,num2))
        elif select_operation=='5':
                print(num1,"**",num2,"=",exponent(num1,num2))
        else:
            #Informs the user to enter a valid operation

            print("ENTER A VALID OPERATION FROM (1-6)")
#check wheather the user want another operation or not
#the loop will break if the answer will be no
        next_calculation=input("LET'S DO ANOTHER CALCULATION?(YES/NO):")
        if next_calculation.upper()=='NO':
            break
       
calculator()
                
            
            
            
