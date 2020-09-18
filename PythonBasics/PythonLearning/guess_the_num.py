n = 18
guesses = 9

attempt = 0
print("*****Guess the number*****")
print("you have", guesses, "guesses left")
while attempt < guesses:
    guess = int(input("Guess the number: "))
    if guess == n:
        print("You guessed correct", "\nNo. of guesses you took to finish:", attempt)
        break
    else:
        attempt += 1
        if guess > n:
            str = "smaller"
        else:
            str = "larger"
        print("The correct number is", str, "than the target number" "\nNo. of guesses left:", guesses - attempt)
print("***Game Over***")