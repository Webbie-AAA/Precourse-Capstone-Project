import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ''
for i in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

lives = 6

correct_letters = []

while True:

    guess = input("Please choose a letter: ")
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ''
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+= letter
        else:
            display += '_'
    if display == chosen_word:
        print("Congrats you won!")
        break
    print(display)
    if guess not in display:
        lives -= 1
        print(f"You guessed {guess}, it isn't in the word. You lose a life.")
        print(hangman_art.stages[lives])
        print(f"\n\t###{lives}/6 left###\n")
    if lives == 0:
        print('you lose')
        print(f"\n\tThe correct word was {chosen_word}\n")
        break
