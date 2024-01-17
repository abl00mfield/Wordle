import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# reading in file of words into a list, stripping newline from end
wordList = [line.rstrip() for line in open('words.txt')]


# setting up variables
wordGuess = ''
gameOn = True
playerWon = False
play = ''
colorList = ['B', 'B', 'B', 'B', 'B']


def printWord(colorList, word):
    '''Takes in 2 parmeters, a list of strings with colors and a string that will be printed
     with backgrounds in those colors with white text'''
    word = word.upper()
    for i, char in enumerate(word):
        if (colorList[i] == 'B'):
            print(Back.BLACK + Fore.WHITE + " " + char + " ", end="")
        elif (colorList[i] == 'Y'):
            print(Back.YELLOW + Fore.WHITE + " " + char + " ", end="")
        else:
            print(Back.GREEN + Fore.WHITE + " " + char + " ", end="")

    print('\n')
    return None


def validWord(word, wordList):
    '''Takes in 2 parameters, a word and a list of words.  
    Returns true if the word is in the list, false if not'''
    word = word.lower()
    return word in wordList


def createColorList(colorList, word, secretWord):
    '''Takes in a colorList, word guess, and the secret word
    returns a colorList with colors that pertain to the guess'''
    colorList = ['B', 'B', 'B', 'B', 'B']
    for i in range(len(word)):  # mark all the green letters first, helps with duplicate letters
        if word[i] == secretWord[i]:
            colorList[i] = "G"

    for i in range(len(word)):
        # find out how many of the same character in the guessed word up to the point we are checking
        charsInWord = multipleLetters(word[i], word[:i+1])
        letterFound = False
        # find out how many of that character are in the secret word
        charsInSecretWord = multipleLetters(word[i], secretWord)
        for j in range(len(secretWord)):
            # checking for yellow letters and making sure that letter isn't already green
            if (i != j and word[i] == secretWord[j] and colorList[j] != 'G'):
                letterFound = True
            # checking for yellow letters and duplicates and making sure letter isn't already green
            if (charsInWord <= charsInSecretWord and letterFound and colorList[i] != 'G'):
                colorList[i] = "Y"
    return colorList


def multipleLetters(char, word):
    '''Takes in a char and a string returns the number of 
    times the char appears in the string'''
    return word.count(char)


while gameOn:
    index = random.randint(0, 2308)  # generating random number to pick word
    secretWord = wordList[index]
    secretWord = secretWord.upper()
    # print(secretWord)
    play = ''
    print("Try and guess my secret word in 6 Guesses")
    print("If you have the letter in the correct spot, it will be green")
    print("If the letter is in the word, but not in the correct spot, it will be yellow")
    print("If the letter is not in the word, it will be black")

    for turn in range(6):
        print(f"You have {6-turn} guesses left\n")
        wordGuess = ''
        while len(wordGuess) != 5:
            wordGuess = input("Please enter a 5 letter word: ")
            wordGuess = wordGuess.upper()
            if len(wordGuess) == 5:
                if not (validWord(wordGuess, wordList)):
                    print("That is not a valid wordle word")
                    wordGuess = ''
            else:
                print("You didn't enter a 5 letter word, try again")
        CL = createColorList(colorList, wordGuess, secretWord)
        if (wordGuess == secretWord):
            if turn == 0:
                print("YOU DID IT IN 1 TRY!! SUPER LUCKY!")
            else:
                print(f"YOU DID IT IN {turn+1} TRIES!")
            printWord(CL, wordGuess)
            playerWon = True
            break
        else:
            printWord(CL, wordGuess)

    if not playerWon:
        print("Sorry, you did not guess the word, the correct word is:")
        printWord(colorList, secretWord)

    while not (play == 'Y' or play == 'N'):
        play = input("Do you want to play again? Y or N? ")
        play = play.upper()
        if play == 'Y':
            gameOn = True
        elif play == 'N':
            gameOn = False
