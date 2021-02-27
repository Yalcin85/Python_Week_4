import random, time

print("Welcome to number guessing game")

tries = 0

a = int(input("Enter min number: "))
b = int(input("Enter min number: "))

num = random.randint(a, b)
beginTime = time.time()

while True:
    guess = int(input("Guess the number between " + str(a) + " and " + str(b) + "\n"))
    tries += 1
    if guess > num:
        print("Missed! Go Lower...")
    elif guess < num:
        print("Missed! Go Higher...")
    else:
        print("Congrats, you find it :)")
        passedTime = time.time() - beginTime
        print(str(tries) + " tries" + " and " + str(int(passedTime)) + " seconds")
        print("Bye bye ")
        break
