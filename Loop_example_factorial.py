'''The factorial function takes as input an integer n and outputs
the factorial (n!) of that number'''
def factorial(n):
    if n == 0: # 0!=1
        x = 1
    else:
        x = 1
        for i in range(0,n):
            x = x*(i+1)
    return x


'''Example usage of function to find the factorial of a user input'''
a = int(input('Enter an integer for which you would like to know the factorial: '))
b = factorial(a)
print ('The factorial of ' + str(a) + ' is ' + str(b) )