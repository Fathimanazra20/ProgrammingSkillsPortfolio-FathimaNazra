# Exercise 05

#Instructions:
#Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#Input Handling: Ask the user to input the month number.
#Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

#Advanced Requirement:
#Leap Year Adjustment: Modify the program to account for leap years. 
#For February, ask the user if the year is a leap year and adjust the number of days accordingly.

# creating a dictionary
days_in_month = {
1: 31,
2: 29,
3: 31,
4: 30,
5: 31,
6: 30,
7: 31,
8: 31,
9: 30,
10: 31,
11: 30,
12: 31
}

year = int(input("Enter a year: ")) 
if year % 4 == 0: 
    print("This is a Leap Year.")
    month_number = int(input("Enter a month number (1-12): "))  
    if month_number in days_in_month:
        print(f"{days_in_month[month_number]} days")
    else:
        print("Invalid month number.")
else:  
    print("This is not a Leap Year.")
    month_number = int(input("Enter a month number (1-12): ")) 
    if month_number == 2: 
        print("28 days")
    elif 1 <= month_number <= 12:
        print(f"{days_in_month[month_number]} days")
    else:
        print("Invalid month number.")