class WordLengthError(Exception):
    pass
class SingleLengthError(Exception):
    pass

def Anagram(first_word, second_word):

    #testing the inputs
    try:
        
        if len(first_word) == 1 or len(second_word) == 1:
            raise SingleLengthError
        elif len(first_word)!= len(second_word):
            raise WordLengthError
        List1 = []
        List2 = []

        #string to list conversion
        for alpha in first_word:
            List1.append(alpha)
        for alpha in second_word:
            List2.append(alpha)


        #checking whether the word is an anagram or not.
        for alpha in List1:
            if alpha in List2:
                List2.remove(alpha)
            else:
                print("The word: ", second_word," is not an anagram of the word:", first_word)
                return
        print ("The word: ", second_word," is an anagram of the word: ", first_word)
        
    except WordLengthError:
        print("Length of the two words are not the same.\nPlease try again!")
    except SingleLengthError:
        print ("Length of the each word must be more than 1\nPlease try again!")
        
        




first_word = input("Enter your first word\n")
second_word = input("Enter your second word\n")
Anagram(first_word, second_word)



