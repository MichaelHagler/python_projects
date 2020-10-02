# Make 6 guesses to solve the hidden word or get hung.
import random

words = ["pie", "programmer", "python"]
quit = False
hidden_word = random.choice(list(words))
guess_counter = 0

#shows how many letters are in the word
print("_ "*(len(hidden_word)))
print(f"""The hidden word is {len(hidden_word)} letters""")


while guess_counter < 6:
    guess = input("Guess a letter. ")

    # check if letter is in hidden_word
    for char in hidden_word:
        if guess != char in hidden_word:
            print("incorrect guess")
            guess_counter += 1


    if guess == hidden_word:
        print(hidden_word)
        print("You guessed the word, you win!")
        break

    elif guess != hidden_word:
        guess_counter += 1
        print(f"That letter does NOT appear in the word try again. {guess_counter} out of 6 guesses.")



    else:
        break
if guess_counter == 6:
    print("You have run out of guesses, you lose!")
