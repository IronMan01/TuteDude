# Take score input from the user
score = int(input("Enter the score (0-100): "))

# Use if-else to determine the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the result
print(f"The grade for score {score} is: {grade}")



# 💡 How It Works:
# The program gets a number from the user (int(input(...))).

# It checks the range using if, elif, and else.

# The highest matching condition is selected and the corresponding grade is printed.





####################################################################################################################################################

# Step 1: Create the dictionary to store student grades
student_grades = {}

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Save to file and exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} not found.")

    elif choice == '3':
        if not student_grades:
            print("No student data available.")
        else:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")

    elif choice == '4':
        # Step 3: Write to a file
        with open("student_grades.txt", "w") as file:
            for name, grade in student_grades.items():
                file.write(f"{name}: {grade}\n")
        print("Student grades saved to 'student_grades.txt'. Exiting.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")




#💡 How It Works:
#The program loops until the user chooses to exit.

#It uses if-else statements for menu selection.

#It saves the final student grades to a file named student_grades.txt.



####################################################################################################################################################


# Use open() to create or open the file in write mode
file = open("my_text_file.txt", "w")

# Use write() to write content to the file
file.write("This is the first line in the file.\n")
file.write("We are writing this using Python file functions.\n")
file.write("File handling is simple with open() and write().\n")

# Close the file to save changes
file.close()

print("Content has been written to 'my_text_file.txt'.")





# How It Works:
# open("filename", "w"): Opens the file in write mode. If the file doesn't exist, it is created. If it exists, contents are overwritten.

# write("text"): Writes the specified text to the file.

# close(): Closes the file to ensure content is saved properly.





####################################################################################################################################################


# Open the file in read mode
file = open("my_text_file.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content to the screen
print("File content:\n")
print(content)

# Close the file
file.close()




# Notes:
# "r" mode stands for read mode.

# file.read() reads the whole content of the file as a single string.

# Always use file.close() to properly close the file.