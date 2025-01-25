start = input("Do you want to start the quiz game? (yes/no) ")
if start.lower() == "yes":
    print("Let's start the quiz game!")
    print("Question 1: What is the capital of France?")
    print("a) Paris")
    print("b) London")
    print("c) Berlin")
    answer = input("Enter your answer: ")
    if answer.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Paris.")
if start.lower() == "no":
    print("Okay, maybe next time!")
print("question 2 : What is the capital of India?")
print("a) New Delhi")
print("b) Mumbai")
print("c) Kolkata")
answer = input("Enter your answer: ")
if answer.lower() == "a":
    print("Correct!")
else:
    print("Incorrect! The correct answer is New Delhi.")