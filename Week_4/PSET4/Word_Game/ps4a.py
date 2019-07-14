# The 6.00 Word Game

import random
import string
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    with open("words.txt", "r") as file:
        valid_words = file.readlines()
        for i in range(len(valid_words)):
            valid_words[i] = valid_words[i].strip().lower()
    print("Loading word list from file...")
    print("{} words loaded".format(len(valid_words)))
    file.close()
    return valid_words
        
            
 
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    frequency = dict()
    for element in sequence:
        if element not in frequency:
            frequency[element] = sequence.count(element)
        
    return frequency
        

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
            score += SCRABBLE_LETTER_VALUES.get(letter, 0)
    score *= len(word)
    if len(word) == n: score += 50
    
    return score
        


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for key in hand:
        for i in range(hand.get(key, 0)):
            print(str(key), end= " ")



def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    count = 0 

    while True:
        hand = dict()
        for i in range(n):
            x = chr(random.randrange(26) + 97)
            hand[x] = hand.get(x, 0) + 1
        
        for letter in VOWELS:
            count += hand.get(letter, 0)
        
        if count >= n//3:
            break
    return hand


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = copy.copy(hand)
    for letter in word:
        if updated_hand.get(letter, 0) > 0:
            if updated_hand.get(letter, 0) == 1:
                del updated_hand[letter]
            elif updated_hand.get(letter, 0) > 1:
                updated_hand[letter] = updated_hand.get(letter, 0) - 1
    return updated_hand


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    h2 = copy.copy(hand)
    if word in wordList:
        for letter in word:
            if letter in h2:
                if h2.get(letter) > 1:
                    h2[letter] = h2.get(letter) - 1
                elif h2.get(letter) == 1:
                    del h2[letter]
            else:
                return False
        return True
    else:
        return False




def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    x = 0
    for letter in hand:
        x += hand.get(letter, 0)
    return x


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total = 0
    
    while True:
        
        if calculateHandlen(hand) == 0:
            print()
            print("Run out of letters. Total score:  {}  points.".format(total))
            return 
        
        else:
            print("Current Hand: ", end="")
            displayHand(hand)
        
            userWord = input('Enter word, or a "." to indicate that you are finished: ')
        
            if userWord == '.':
                print("Goodbye! Total score:  {}  points.".format(total))
                return
        
            else:
                if isValidWord(userWord, hand, wordList):
                    score = getWordScore(userWord, n)
                    total += score
                    print('"{}" earned {}  points. Total:  {}  points'.format(userWord, score, total))
                
                    hand = updateHand(hand, userWord)
                else:
                    print("Invalid word, please try again.")
                    print()                    
        

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    programcounter = 0
    while True:
    
        userin = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if userin == 'e':
            break
        elif userin == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            programcounter += 1
        
        elif userin == 'r' and programcounter == 0:
            print("You have not played a hand yet. Please play a new hand first!")
        
        elif userin == 'r' and programcounter != 0:
            playHand(hand, wordList, HAND_SIZE)
        
        else:
            print("Invalid command.")
            
    
        
    
   




if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
