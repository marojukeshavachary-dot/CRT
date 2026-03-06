'''
Debugging in Python
 bug -->Error
 Debugging-->Finding and fixing the Errors
    Types of Errors:  
        1. Syntax Error
        2. Logical Error
        3. Runtime Error
        
    1. Syntax Error:
        - Missing of colon, missing of indentation 
        - Example:
            print("Hello World"
    2. runtime Error:
        - Division by zero(0)
        - Example:
            a = 10
            b = 0
            print(a/b)
    3. Logical Error:
        - Missing of LOgics
        - Example:
            def add(a, b):
                return a - b  # Logical error here
            print(add(5, 3))  # Expected output is 8, but will get 2
            
    Debugging Techniques:
        1. Print Statement Debugging:
            - Inserting print statements to check variable values at different stages.
        2. Using Debugger:
            - Using built-in debuggers like pdb in Python to step through the code.
        3. Code Reviews:
            - Having another set of eyes look at the code to catch errors you might have missed.
        4. Rubber Duck Debugging:
            - Explaining your code line-by-line to an inanimate object to find logical errors.
            
    purpouse :
        1. pause the exicution
        2. inspect the variable values
        3. To run the code line by line
        
    pdb commands:
        -n --> To execute the output in a next line
        -p variable -->To get the value of a variable 
        -l --> List nearby code
        -c --> continue the execution
        -s --> To start a function 
        -r --> return from the function 
        -h --> help 
        -q --> Quit the debugger
(code example)
try:
    a = int(input("Enter a number: "))
    print(10/0) 
except ZeroDivisionError:
    print ("can not divisible in Zero")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    ''' 

import pdb

def add(a, b):
    pdb.set_trace()  
    return a + b 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a,b))
