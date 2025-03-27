sum = 0

def my_func(n):
    """This is a recursive function calculates this formula = 1 + 1/2 + 1/3 + .... + 1/n"""
    global sum

    if n <= 0:
        return
    
    sum += 1/(n)
    my_func(n-1)
