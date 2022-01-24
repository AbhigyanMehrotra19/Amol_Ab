def Anagram(first_word, second_word):

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


first_word = input("Enter your first word")
second_word = input("Enter your second word\n")
Anagram(first_word, second_word)



