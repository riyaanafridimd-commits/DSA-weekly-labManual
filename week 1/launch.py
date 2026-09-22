'''def add_numbers(num1,num2):
    sum = num1 + num2
    print("sum: ",sum)
add_numbers(5,8)'''

'''
def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)'''



'''def outer():
    message = 'local'
  
    def inner():
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()'''



def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))



















