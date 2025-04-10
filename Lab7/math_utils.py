def add(x, y):
    return int(x) + int(y)

def subtract(x, y):
    return int(x) - int(y)

def multiply(x, y):
    return int(x) * int(y)

def divide(x, y):
    try:
        return float(int(x) / int(y))
    except ZeroDivisionError:
        print("Division by zero!")
        return None

def power(x, y):
    return int(x) ** int(y)

def mod(x, y):
    return int(x) % int(y)

if __name__ == "__main__":
    print(f"Test Case 1: Add 5 + 3: {add(5, 3)}")
    print(f"Test Case 2: Subtract 10 - 4: {subtract(10, 4)}")
    print(f"Test Case 3: Multiply 3 * 7: {multiply(3, 7)}")
    print(f"Test Case 4: Divide 20 / 5: {divide(20, 5)}")
    print(f"Test Case 5: Divide 5 / 0: {divide(5, 0)}")
    print(f"Test Case 6: Power 2 ** 3: {power(2, 3)}")
    print(f"Test Case 7: Mod 10 % 3: {mod(10, 3)}")