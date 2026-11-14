
# Student Mark Management System
# Modified Version - Average and Pass/Fail

name = input("Enter Student Name: ")

mark1 = int(input("Enter Subject 1 Marks: "))
mark2 = int(input("Enter Subject 2 Marks: "))
mark3 = int(input("Enter Subject 3 Marks: "))

# Calculate total marks
total = mark1 + mark2 + mark3

# Calculate average marks
average = total / 3

# Check pass or fail
if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    result = "PASS"
else:
    result = "FAIL"

# Display student details
print("\n----- STUDENT MARK REPORT -----")
print("Student Name:", name)
print("Subject 1 Marks:", mark1)
print("Subject 2 Marks:", mark2)
print("Subject 3 Marks:", mark3)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Result:", result)
