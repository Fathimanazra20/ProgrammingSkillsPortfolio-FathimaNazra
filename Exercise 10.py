# Exercise 10

#steps:
#The program should ask the user for a number from within the main function.
#The entered number should be passed to a function that determines if the value is even or odd.
#The function should return a message indicating whether the number is even or odd.
#The message returned by the function should be printed from within the main function.

def check_even_or_odd():
    num=int(input("enter a number: "))
    if num % 2 == 0:
        print("this is an even number")
    else:
        print("this is an odd number")    
check_even_or_odd()        