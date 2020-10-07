# Make 6 guesses to solve the hidden word or get hung.
import random

words = ["pie", "programmer", "python"]
correct_guesses = []
wrong_guesses = []
hidden_word = random.choice(list(words))
guess_counter = 6

#shows how many letters are in the word
print("_ "*(len(hidden_word)))
print(f"""The hidden word is {len(hidden_word)} letters""")


while guess_counter > 0:
    guess = input("Guess a letter. ")

    # check if letter is in hidden_word
    for char in hidden_word:
        if char == guess:
            correct_guesses.append(guess)
            print(f"{guess} is right! This is what you've guessed right so far:", *correct_guesses)

        elif guess != char:
            wrong_guesses.append(guess)
            print(f"{guess} was wrong. This is what you've guessed wrong so far:", *wrong_guesses)
            guess_counter -= 1
            print(f"You have {guess_counter} guesses left.")



    if guess == hidden_word:
        print(hidden_word)
        print("You guessed the word, you win!")
        break


if guess_counter == 0:
    print("You have run out of guesses, you lose!")
