word = "secret"

errors = 9

guesses = []

game = False

while not game:

    for letter in word:

        if letter.lower() in guesses:
            print(letter,end=" ")

        else:
            print("_",end=" ")

    print("")



    guess = input(f"allowed errors left {errors},next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        errors = errors - 1

        if errors == 0:
            break

    game = True

    for letter in word:
        if letter.lower() not in guesses:
            game = False

if game:
    print(f"you found the word and the word is {word}")
else:
    print(f"game over and the word is  {word}")


