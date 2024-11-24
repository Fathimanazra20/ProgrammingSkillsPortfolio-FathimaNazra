# Exercise 06

#steps:
#Define the correct password.
#Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#Output an appropriate message when the correct password is entered.

password="12345"
while password=="12345":
    password=input("enter password: ")
    if password=="12345":
        print("correct password")
        break
    else:
        print("incorrect password. try again!")