while True:
    guess = input("Guess a letter")
    if len(guess)==1 and guess.isalpha():
        break
    else:
        "Invalid letter. Please, enter a single alphabetical character."