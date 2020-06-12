import string
from words import choose_word, load_words
from images import IMAGES 
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    sum = 0
    for i in range(len(secret_word)):
        if(letters_guessed.count(secret_word[i]) > 0):
            sum += letters_guessed.count(secret_word[i])
    if(sum== len(secret_word)):
        return True
    else:
        return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    
    '''
    test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    main_list = []
    for i in test_list:
        if(letters_guessed.count(i)==0):
            main_list.append(i)
    string1=""
    string1=string1.join(main_list)
    letters_left = string1.lower()
    return letters_left

def display_hint(letters_guessed):
    res=[]
    test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    for i in test_list:
        if(letters_guessed.count(i)==0):
            res.append(i)
    for i in res:
        if(secret_word.count(i)>0):
            return i

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    letters_guessed = []

    remaining_lives = 8
    hint =True
    while remaining_lives>0:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        print("Remaining lives: {} ".format(remaining_lives))
        guess = str(input("Please guess a letter: "))
        letter = guess.lower()
        if(letter=='hint' and hint==True):
            hint=False
            print(display_hint(letters_guessed))
        elif(len(guess)>1 or ord(letter) < ord('a') or ord(letter) > ord('z')):
            print(letter)
            remaining_lives-=1
        else:
            if letter in secret_word:
                letters_guessed.append(letter)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print(" * * Congratulations, you won! * * ", end='\n\n')
                    return
                    
            else:
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                letters_guessed.append(letter)
                remaining_lives-=1
                print(IMAGES[7-remaining_lives])

        


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
word_list=load_words()
secret_word = choose_word()
#secret_word='distort'
hangman(secret_word)
#print(secret_word)

