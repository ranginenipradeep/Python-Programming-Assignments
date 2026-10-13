#Q2
marks = [78,35,92,40,61]
print("Marks:", marks)
print( "Highest mark:", max(marks))
print("Lowest mark:", min(marks))

count = 0
for mark in marks:
    if mark >= 40:
        count += 1
print("Students scoring at least 40:", count)

valid = min(marks) >= 0 and max(marks) <= 100
print("All marks are valid:", valid)

marks[0] = 85
print("Updated Marks:", marks)


