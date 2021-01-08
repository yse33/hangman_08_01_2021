#gospodine, daje izmislih hitrost kak da printvam i ako nqkoq ot srednite bukvi e sushtata kato purvata ili poslednata
from os import system, name 
def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
word = input("Enter a word here: ")
clear()
lenght = len(word)
guesses = ''
turns = 8
while turns > 0:
    mistakes = 0
    for i in word:
        if i == word[0] or i == word[lenght-1]:
            print(i)
        elif i in guesses:
            print(i)
        else:
            print("_")
            mistakes += 1
    if  mistakes == 0:
        print("You guessed the word!")
        print("The word was:", word)
        break
    guess = input("Enter a letter to guess: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("This letter is not in the word")
        if turns != 0:
            print("You have", + turns, "more tries")
        else:
            print("You loose")
            print("The word was:", word)
    