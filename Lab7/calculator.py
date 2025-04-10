import math_utils

num_one = input("Please enter the first number: ")
num_two = input("Please enter the second number: ")
operator = input("Please enter an operator (+, -, *, /, **, %): ")

o_to_funcs = {"+" : math_utils.add, "-" : math_utils.subtract, "*" : math_utils.multiply, "/" : math_utils.divide, "**" : math_utils.power, "%" : math_utils.mod}

try:
    if operator in o_to_funcs:
        result = o_to_funcs[operator](num_one, num_two)
        if result is not None:
            print(f"Result is {result}")
    else:
        print(f"Invalid operator: {operator}")

except ValueError:
    print("Please enter valid numbers!")


if __name__ == "__main__":
    
    test_cases = [
        (5, 3, "+"),      
        (10, 4, "-"),     
        (6, 7, "*"),      
        (20, 5, "/"),     
        (10, 0, "/"),     
        (2, 3, "**"),     
        (10, 3, "%"),     
        (5, 2, "&")       
    ]
    
    for num1, num2, op in test_cases:
        print(f"\nTest: {num1} {op} {num2}")
        
        try:
            if op in o_to_funcs:
                result = o_to_funcs[op](num1, num2)
                if result is not None:
                    print(f"Result is {result}")
            else:
                print(f"Invalid operator: {op}")
        except ValueError:
            print("Please enter valid numbers!")
    