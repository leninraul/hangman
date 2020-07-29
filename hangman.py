
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result=True
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            result=False  
    return result  
            
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=''
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            result+='_ ' 
        else:
            result+=secretWord[i]
    return result  

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result=list(string.ascii_lowercase)    
    for letter in list(string.ascii_lowercase):      
        if letter in lettersGuessed:
            result.remove(letter)
    return ''.join(result)
    
def guessed():
    '''
    input: string, any letter
    returns: string, that same letter in lowercase or an error 
        message if input wasn't a anything else than a single letter.
    
    '''
    
    import string
    done=False
    while not done:
        guess=input("Please guess a letter: ")
        guessed_letter=guess.lower()
        if guessed_letter in list(string.ascii_lowercase):
            done=True
        else:
            print('Only a letter!')
    return guessed_letter

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print('-------------')
    guesses_left=8
    lettersGuessed=[]
    while guesses_left>0 and isWordGuessed(secretWord, lettersGuessed)==False:
      
        print('You have '+str(guesses_left)+' guesses left.')
        print('Available letters: '+getAvailableLetters(lettersGuessed))
        
        guessed_letter=guessed()      
                
        if guessed_letter in lettersGuessed:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            guesses_left=guesses_left
            print('-------------')
        else:
            lettersGuessed.append(guessed_letter)
            if guessed_letter in list(secretWord):
                print('Good guess: '+getGuessedWord(secretWord, lettersGuessed))
                guesses_left=guesses_left
                print('-------------')
            else:    
                print('Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed))
                guesses_left-=1
                print('-------------')
                
    if isWordGuessed(secretWord, lettersGuessed)==True:
        return print('Congratulations, you won!')
    else:
        return print('Sorry, you ran out of guesses. The word was '+secretWord+'.')
        

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
