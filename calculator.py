def add(num1, num2):
    added_sum = (num1 + num2)
    print(added_sum)

def subtract(num1, num2):
    subtracted_sum = (num1 - num2)
    print(subtracted_sum)

def divide(num1, num2):
    divided_sum = (num1/num2)
    print(divided_sum)

def multiply(num1, num2):
    multiplied_sum = (num1 * num2)
    print(multiplied_sum)


while True:
    exit_choice = input("Would you like to continue? Press Y for yes and N for no. " )
    if(exit_choice == "Y"):
        pass
    
    if(exit_choice == "N"):
        exit()
    # when I am defining a variable, in this case exit choice on line 19, I do not indent for that.
    # I indent when I am carrying out an operation.
    num1 = int(input("Please enter the first number that you wish to calculate. " ))
    function_choice = input("Please press + for addition, - for subtraction, * for multiplication, / for division. ")
    num2 = int(input("Please enter the second value you wish to calculate "))

    if(function_choice == "+"):
        add(num1, num2)

    elif(function_choice == "-"):
        subtract(num1, num2)

    elif(function_choice == "*"):
        multiply(num1, num2)

    elif(function_choice == "/"):
        divide(num1, num2)
    
    else:("Please enter one of the +,-,*, or /.")
    # get this program to continue to ask the user if they want to calculate again. 



# complted:  start by saying the calculation is at 0 and would ask the user to input a number and the functions it wants to run
# I need it to store the input and than I need functions to calculate. 
# 0-9 numbers 
# adding function
# subtracting function
# multiplication
# division 
# positive and negative number convertor. 
# needs numbers to select
# clear button
# percent button 
# equals button
# period button 
# an interface to show the person what they are typing and calculating 


# it runs the functions. maybe something like an if else statement for +,-,*,/ 
# it prints it out and than asks the user if it should do something else. 
# it will continue to ask it to do those functions until the user is satsified. 

# and than there should be a break to end the if elif stuff.
# and than it should clear.


#other functionality would be exponents. 
# maybe importing from that numpy or python libraries. 