import random
import string

letters_and_replacements = {}
rep_chars = set()

print("Choose 5 characters (lowercase only) and assign 3 replacement options each: ")

for i in range(5):
    while True:
        letter = input("Enter a lowercase character: ")
        if len(letter) == 1 and letter.islower():
            if letter in letters_and_replacements:
                print("You chose this letter. Please enter a different one!")
            else:
                break
        else:
            print("Please enter a single lowercase character!")
    
    replacements = []
    while len(replacements) < 3:
        replacement = input(f"Enter a replacement for '{letter}': ")
        if len(replacement) == 1:
            if replacement in rep_chars:
                print("You chose this replacement. Please enter a different one!")
            else:
                replacements.append(replacement)
                rep_chars.add(replacement)
        else:
            print("Please enter a single replacement!")
    
    letters_and_replacements[letter] = replacements

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    
    generated_password = ""
    replacement_count = 0
    
    for char in password:
        if char in letters_and_replacements:
            replacement = random.choice(letters_and_replacements[char])
            generated_password += replacement
            replacement_count += 1
        else:
            generated_password += char
    
    passwords.append((generated_password, replacement_count))

categorized_passwords = {"strong": [], "weak": []}

for password, count in passwords:
    if count > 4:
        categorized_passwords["strong"].append(password)
    else:
        categorized_passwords["weak"].append(password)

print("\nGenerated passwords: ")

print("\nSTRONG PASSWORDS: ")
for strong_password in categorized_passwords["strong"]:
    print(strong_password)

print("\nWEAK PASSWORDS: ")
for weak_password in categorized_passwords["weak"]:
    print(weak_password)

