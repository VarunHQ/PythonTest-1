name = input("Enter your name: ")
attempts = 5
secret = 12
hint = "If the secret number is in celsius it will be Cold🥶"

print(hint)

while attempts > 0:
    user_guess = int(input("Enter your guess of the number. You only have 5 attempts: "))

    if user_guess == secret:
        print("Congratulations, " + name + "! You have guessed the number correctly!")
        break
    elif user_guess < secret:
        print("Your guess is too low. Try again.")
        attempts -= 1
        print("Attempts left:", attempts)
    else:
        print("Your guess is too high. Try again.")
        attempts -= 1
        print("Attempts left:", attempts)

if user_guess != secret:
    print("=====     =====")
    print("Sorry, " + name + ", you've run out of attempts. The secret number was:", secret)
    print("Better luck next time! 🎯")
    print("===== Thank you for playing! =====")

if user_guess == secret:
    print("=====     =====")
    print("Bravo, " + name + "! Well done! You are an expert guesser! 🏆")
    print("===== Thank you for playing! =====")
