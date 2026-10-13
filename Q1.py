# username = input("Enter your username: ")

# if len(username) < 5:
#     print("Username must be at least 5 characters long.")
# elif username.strip() == "":
#     print("Username cannot be empty or just whitespace.")
# elif username.lower() == "admin":
#     print("Username cannot be 'admin'.")
# else:
#     print("Username is valid.")


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