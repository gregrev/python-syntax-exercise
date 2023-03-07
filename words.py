def print_upper_words(words, must_start_with={'a','b'}):
    """for a list of words, print out each word on a separate line, but in all uppercase"""
    # .upper() 

    for word in words:
        if word[0] in must_start_with:
            print(word.upper())
    

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"g", 'h', 'y'})