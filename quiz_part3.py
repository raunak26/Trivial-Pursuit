# quiz_part3.py
# Raunak Anand  
# ECS32A Fall 2018
#
# This code responds to your answer to a trivia question depending on whether your answer is right or wrong


# welcome message
print("Trivial Pursuit 12 Questions\n")
score = 0

print("ART AND LITERATURE: Who painted the Mona Lisa?")  # Question 1
# options 1
print("a. Vincent van Gogh")
print("b. Michelangelo")
print("c. Leonardo da Vinci")
# answer is c
answer = input("Enter your choice:")
if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")

print("ART AND LITERATURE: What did the 7 dwarves do for a job?")  # Question 2
# options 2
print("a. construction workers")
print("b. miners")
print("c. fishers")
# answer is b
answer = input("Enter your choice:")
if answer == "b":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was b")

print('ENTERTAINMENT: Who sang "My Way"?')  # Question 3
# options 3
print('a. Gordon Jenkins')
print('b. Louis Armstrong')
print('c. Frank Sinatra')
# answer is c 
answer = input("Enter your choice:")
if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")

print("ENTERTAINMENT: How many oscars did Alfred Hitchcock win?")  # Question 4
# options 4
print("a. 0")
print("b. 1")
print("c. 2")
# answer is a
answer = input("Enter your choice:")
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

print("GEOGRAPHY: Which is the largest ocean?")  # Question 5
# options 5
print("a. Pacific")
print("b. Atlantic")
print("c. Indian")
# answer is a
answer = input("Enter your choice:")
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

print("GEOGRAPHY: Which river goes through London?")  # Question 6
# options 6
print("a. River Severn")
print("b. River Tyne")
print("c. River Thames")
# answer is c
answer = input("Enter your choice:")
if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")

print("HISTORY: What year did the Spanish Civil War end?")  # Question 7
# options 7
print("a. 1937")
print("b. 1939")
print("c. 1945")
# answer is b
answer = input("Enter your choice:")
if answer == "b":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was b")
      
print("HISTORY: Who was the first president of America?")  # Question 8
# options 8
print("a. Washington")
print("b. Lincoln")
print("c. Jefferson")
# answer is a 
answer = input("Enter your choice:")
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

print("SCIENCE AND NATURE: Who invented the telephone?")  # Question 9
# options 9
print("a. Bell")
print("b. Edison")
print("c. Tesla")
# answer is a
answer = input("Enter your choice:")
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

print("SCIENCE AND NATURE: Where is the smallest bone in the body?")  # Question 10
# options 10
print("a. Ear")
print("b. Nose")
print("c. Finger")
# answer is a
answer = input("Enter your choice:")
if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

print("SPORT AND LEISURE: What is the first letter on a typewriter?")  # Question 11
# options 11
print("a. Z")
print("b. A")
print("c. Q")
# answer is c
answer = input("Enter your choice:")
if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")

print("SPORT AND LEISURE: How many months have 31 days?")  # Question 12
# options 12
print("a. 5")
print("b. 6")
print("c. 7")
# answer is c
answer = input("Enter your choice:")
if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")

print("Your final score is", score, "out of 12")
if score < 5:
      print("You were unlucky!")
elif score >= 5 and score <= 8:
      print("You did better than chance!")
elif score >= 9 and score <= 11:
      print("You are a trivia star")
else :
      print("Perfect!")
      


