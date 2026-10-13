
# Create a list of students' marks
marks = [78, 35, 92, 40, 61]

# Display the original marks
print("Marks:", marks)

# Find and display the highest mark
print("Highest mark:", max(marks))

# Find and display the lowest mark
print("Lowest mark:", min(marks))

# Initialize the count to zero
count = 0

# Check each mark in the list
for mark in marks:
    # Count students who scored at least 40
    if mark >= 40:
        count += 1

# Display the number of students scoring at least 40
print("Students scoring at least 40:", count)

# Check whether all marks are between 0 and 100
valid = min(marks) >= 0 and max(marks) <= 100

# Display whether all marks are valid
print("All marks are valid:", valid)

# Update the first mark from 78 to 85
marks[0] = 85

# Display the updated marks
print("Updated Marks:", marks)


