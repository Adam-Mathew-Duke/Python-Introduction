# factorial calculator

def calculate_factorial(number):
    for index in range(number-1,0,-1):
        number = number * index
    return number
    
factorial = print(calculate_factorial(5))
