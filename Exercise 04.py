# Exercise 04

#Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

#Advanced Requirements:
#Ignore Capitalization: Modify your program to accept answers regardless of the capitalization 
#(e.g., "paris", "Paris", and "PaRis" should all be considered correct)
#Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries.
#Provide feedback for each question.

#creating a dictionary
country = {"France": "Paris",
"Germany": "Berlin",
"Italy": "Rome",
"Spain": "Madrid",
"Portugal": "Lisbon",
"Netherlands": "Amsterdam",
"Belgium": "Brussels",
"Austria": "Vienna",
"Switzerland": "Bern",
"Greece": "Athens"}

score=0                                                                
total = len(country)                                                    

for nation, city in country.items():                                    
    response = input(f"What is the capital of {country}? ").strip()     
    if response.capitalize() == city.capitalize():                     
        print("Correct!")
        score += 1                                                    
        print()                                                       
    else:
        print(f"Wrong! The capital of {country} is {city}.")
        print()                                                        
print(f"\nScore: {score}/{total}")                                    
