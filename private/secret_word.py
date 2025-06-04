secret_word = "mine"
max_attempts = 5
attempt = 0
def get_choice():
    choice = input().lower()
    if choice == "yes":
            print(f"\n Awww..............^^ that's so sweet of you.")
            print(f"\n Thank you mine...!! Meet you in your dreams.")
    else:
            print(f"\n Ahh... That's heart breaking...! Thank you for playing with me")
    return
print(" Welcome to 'Guess the word of my love' game!")
print("You have 5 chances to guess the secret the word.")

while attempt < max_attempts:
    guess = input(f"\nAttempt {attempt + 1}: Enter your guess: ").lower()
    attempt += 1

    if guess == secret_word:
        print("Correct! Can I call you mine!")
        print(f"\n Yes or No")
        get_choice()
        break
    elif len(guess) < len(secret_word):
        print("Hmm... Nah! Think emotionally")
    elif len(guess) > len(secret_word):
        print("Oops... It's a love bite!")
    else:
        print("Nope! Try again.")
if guess != secret_word:
    print(f"\n Game over! The correct answer was: {secret_word}")
    print(f"\n Yes.! It's you my love. Can I call you mine?")
    print(f"\n Yes or No")
    get_choice()