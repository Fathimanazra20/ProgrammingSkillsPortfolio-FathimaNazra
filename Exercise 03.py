#Exercise 03: Biography

# steps
# Store the information (name, hometown, and age) as key-value pairs in a dictionary.
# Print the values on separate lines using a single print() statement.
# Use variables with appropriate data types for each piece of information

# Advanced Requirements:
# Have the user input their name, hometown, and age instead of hardcoding the values. 
# Try giving both your first and second name when asked for your name.
# What happens? How can you handle multiple words in Python? Test the program by entering a string value for age (e.g., "twenty")
# What happens? How can you prevent this issue?

name=str(input("enter your name: "))
hometown=str(input("enter your hometown: "))
age=int(input("enter your age:  "))
personal_info = {"name":name, "hometown": hometown, "age": age}
print(personal_info["name"],personal_info["hometown"],personal_info["age"],sep="\n")