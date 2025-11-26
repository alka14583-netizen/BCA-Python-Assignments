# ============================================
# Student Profile Console App
# ============================================

print("\n============================================")
print("     WELCOME TO STUDENT PROFILE SYSTEM")
print("============================================\n")

# ------------------------------
# Task 2: Input & Variables
# ------------------------------

full_name = input("Enter your full name: ")
roll_no = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

print("\n--- User Data Stored Successfully! ---\n")

# ------------------------------
# Task 3: Operators Demonstration
# ------------------------------

print("\n=== Operators Demonstration ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n-- Arithmetic Operators --")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)
print("Floor Division:", num1 // num2)

print("\n-- Assignment Operators --")
x = num1
x += 2
print("x += 2:", x)
x -= 1
print("x -= 1:", x)

print("\n-- Comparison Operators --")
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 == num2:", num1 == num2)

print("\n-- Logical Operators --")
print("(num1 > 10) and (num2 > 10):", (num1 > 10) and (num2 > 10))
print("(num1 > 10) or (num2 > 10):", (num1 > 10) or (num2 > 10))
print("not(num1 > num2):", not(num1 > num2))

print("\n-- Identity Operators --")
print("num1 is num2:", num1 is num2)
print("num1 is not num2:", num1 is not num2)

print("\n-- Membership Operators --")
text_sample = "python programming"
print("'p' in text_sample:", 'p' in text_sample)
print("'z' not in text_sample:", 'z' not in text_sample)

# ------------------------------
# Task 4: String Operations
# ------------------------------

print("\n=== String Operations ===")
print("Uppercase Name:", full_name.upper())
print("Lowercase Name:", full_name.lower())
print("Title Case Name:", full_name.title())
print("Stripped Name:", full_name.strip())
print("Replace spaces with dashes:", full_name.replace(" ", "-"))
print("Count of 'a' in name:", full_name.count("a"))

# ------------------------------
# Task 5: Final Student Profile Output
# ------------------------------

print("\n--------------------------------------------")
print("            STUDENT PROFILE SYSTEM")
print("--------------------------------------------")

print(f"Name:            {full_name}")
print(f"Roll No:         {roll_no}")
print(f"Course:          {program}")
print(f"University:      {university}")
print(f"City:            {city}")
print(f"Age:             {age}")
print(f"Hobby:           {hobby}")

print("--------------------------------------------")
print("Welcome to Python Programming!")
print("--------------------------------------------\n")

# ------------------------------
# Task 6: Bonus - Save to File
# ------------------------------

save = input("Do you want to save your profile? (yes/no): ")

if save.lower() == "yes":
    with open("student_profile.txt", "w") as file:
        file.write("----- Student Profile -----\n")
        file.write(f"Name: {full_name}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Course: {program}\n")
        file.write(f"University: {university}\n")
        file.write(f"City: {city}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hobby: {hobby}\n")
    print("Profile saved successfully as student_profile.txt!")
else:
    print("Profile was not saved.")

print("\nThank you for using the Student Profile App!")
