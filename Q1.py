
# Get the username from the user
username = input("Enter your username: ")

# Check if the username has fewer than 5 characters
if len(username) < 5:
    print("Username must be at least 5 characters long.")

# Check if the username is empty or contains only spaces , works when we type 5 blank spaces 
elif username.strip() == "":
    print("Username cannot be empty or just whitespace.")

# Check if the username is 'admin' (ignoring uppercase/lowercase)
elif username.lower() == "admin":
    print("Username cannot be 'admin'.")

# If none of the above conditions are true, the username is valid
else:
    print("Username is valid.")





