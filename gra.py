import random
my_number = random.randint(0,20)
trails = 0
guess = int(input("Guess my number: "))

while guess != my_number:
    guess = int(input("Guess my number: "))
    if guess > my_number:
        print("My number is smaller, try again")
        trails+=1
        print(trails)
    elif guess < my_number:
        print("My number is bigger, try again")
        trails+=1
        print(trails)
else:
    print("Congratulations, thats my number!")