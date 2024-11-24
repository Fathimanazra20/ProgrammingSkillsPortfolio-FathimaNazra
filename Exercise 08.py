# Exercise 08

#Write a program that searches for a specific string within a list of strings. 
#The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , 
#and your task is to search for "Sam".

names=["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
search_name= input("enter the name in search")
if "Sam" in list(names):
    print("name is there in the list")
else:
    print("name is not there in the list")    