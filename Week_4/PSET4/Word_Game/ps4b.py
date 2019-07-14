import ps4a
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    bestscore = 0
    bestword = None
    for word in wordList:
        if ps4a.isValidWord(word, hand, wordList):
            if ps4a.getWordScore(word, n) > bestscore:
                bestscore = ps4a.getWordScore(word, n)
                bestword = word
    return bestword
    

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0
    
    while True:
        
        if not ps4a.calculateHandlen(hand) or not compChooseWord(hand, wordList, n):
            print("Total score: {} points.".format(total))
            return 
        
        print("Current Hand: ", end="")
        ps4a.displayHand(hand)
        for word in wordList:
            if ps4a.isValidWord(word, hand, wordList):
                score = ps4a.getWordScore(word, n)
                total += score
                print('"{}" earned {}  points. Total:  {}  points'.format(word, score, total))
                hand = ps4a.updateHand(hand, word)
                

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    progcounter = 0
    while True:
        userin = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
        if userin == 'e':
            return
        elif userin == 'n':
            hand = ps4a.dealHand(ps4a.HAND_SIZE)
            choice(hand, wordList)
            progcounter += 1
        
        elif progcounter == 0 and userin == 'r':
            print("You have not played a hand yet. Please play a new hand first!")
        elif progcounter > 0 and userin == 'r':
            choice(hand, wordList)
            
        else: 
            print("Invalid command.")
        

def choice(hand, wordList):
    """ Helps the user choose whether to play themselves or have the computer play"""
    while True:
        comp = input("Enter u to have yourself play, c to have the computer play: ")
        if comp == 'u':
            ps4a.playHand(hand, wordList, ps4a.HAND_SIZE)
            break
        elif comp == 'c':
            compPlayHand(hand, wordList, ps4a.HAND_SIZE)
            break
        else:
            print("Invalid command.")
    return 
    
    
                

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = ps4a.loadWords()
    playGame(wordList)


