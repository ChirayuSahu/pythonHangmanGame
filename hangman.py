import random
words = [
    {"word": "python", "hint": "A popular programming language."},
    {"word": "elephant", "hint": "The largest land animal."},
    {"word": "jupiter", "hint": "The largest planet in the Solar System."},
    {"word": "guitar", "hint": "A stringed musical instrument."},
    {"word": "pyramid", "hint": "An ancient Egyptian structure."}
]

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]

def hangman_game():
    print("Welcome to Hangman!")
    chosen_word = random.choice(words)
    word = chosen_word["word"]
    hint = chosen_word["hint"]
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(display_hangman(tries))
    print(f"Word: {word_completion}")
    print("You can use 'hint' once if you get stuck!")

    while not guessed and tries > 0:
        guess = input("Guess a letter or the full word: ").lower()
        
        if guess == "hint":
            print(f"Hint: {hint}")
            continue
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join(
                    [letter if letter in guessed_letters else "_" for letter in word]
                )
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the correct word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Try again.")

        print(display_hangman(tries))
        print(f"Word: {word_completion}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Game Over! The word was '{word}'. Better luck next time!")

hangman_game()
