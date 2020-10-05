# Make 6 guesses to solve the hidden word or get hung.
import random

words = ["pie", "programmer", "python"]
hidden_word = random.choice(list(words))
guess_counter = 6

#shows how many letters are in the word
print("_ "*(len(hidden_word)))
print(f"""The hidden word is {len(hidden_word)} letters""")


while guess_counter > 0:
    guess = input("Guess a letter. ")

    # check if letter is in hidden_word
    for char in hidden_word:
        if guess in char:
            print(f"{guess} is in the mystery word.")

        else:
            print("Your guess was incorrect")



    if guess == hidden_word:
        print(hidden_word)
        print("You guessed the word, you win!")
        break

    elif guess != hidden_word:
        guess_counter -= 1
        print(f"That letter does NOT appear in the word try again. You have {guess_counter} guesses.")



    else:
        break
if guess_counter == 0:
    print("You have run out of guesses, you lose!")
