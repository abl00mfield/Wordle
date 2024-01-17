# this program was only used to test the functionaliy of the main program

def multipleLetters(char, word):
    '''Takes in a char and a string returns the number of 
    times the char appears in the string'''
    return word.count(char)


def createColorList(colorList, word, secretWord):
    '''Takes in a colorList, word guess, and the secret word
    returns a colorList with colors that pertain to the guess'''

    for i in range(len(word)):
        if word[i] == secretWord[i]:
            colorList[i] = "G"

    for i in range(len(word)):
        charsInWord = multipleLetters(word[i], word[:i+1])
        letterFound = False
        charsInSecretWord = multipleLetters(word[i], secretWord)
        for j in range(len(secretWord)):
            if (i != j and word[i] == secretWord[j] and colorList[j] != 'G'):
                letterFound = True
            if (charsInWord <= charsInSecretWord and letterFound and colorList[i] != 'G'):
                colorList[i] = "Y"
    return colorList


colorList = ['B', 'B', 'B', 'B', 'B']
testList = createColorList(colorList, 'aapaa', 'apbla')

print(testList)
