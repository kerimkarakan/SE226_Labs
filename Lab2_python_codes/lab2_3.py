user_num = int(input("Please enter a number between 3 and 9 (inclusive): "))

if user_num >= 3 and user_num <= 9:
    for i in range(1, user_num + 1):
        print("*" * i)

    for j in range (user_num - 1, 0, -1):
        print ("*" * j)

    


else:
    print("Enter a valid number!")

