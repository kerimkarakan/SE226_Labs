def factorial(x):
    if x <= 0:
        return 1
    return factorial(x-1) * x 

def sine_x(x,n):
    x = x * 3.14/180
    sum = 0
    
    single_step = lambda a: ((-1)**a) * (x**(2*a+1)) / factorial(2*a+1)

    for i in range(n):
        sum += single_step(i)
    
    return sum