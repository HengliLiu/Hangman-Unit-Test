# test_hangman.py

import hangman
import unittest

# A. Getting secret word

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/1.words") == "fireman" for _ in range(100))

# Secret word should have no punctuation

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/2.words") == "policeman" for _ in range(100))

# Secret word should not be a proper noun

# B. Masking secret word    
    
def test_mask_word():
    word = "gangman"
    guess = ""
    assert hangman.mask_word(word, guess) == "*******"

# Masks entire word when not guessed.

def test_mask_word_guessed():
    words = ["python", "tigers","whales"]
    assert all([hangman.mask_word(i, i) == i for i in words])

# Unmasks entire word when fully guessed.

def test_mask_word_repetitive():
    words = ["superman", "batman","fireman" ]
    guess = [ "kuvdga", "fhreuao", "dherpsn"]
    masks = ["*u****a*", "*a**a*" ,"**re**n"]
    assert all([ hangman.mask_word(words[i], guess[i]) == masks[i] for i in range(len(words)) ])

# Unmasks for words with repetitive letters.

# C. Checking inputs

def test_input1():
    guess = [ "you", "we", "u", "i", "v" ]
    result = [("Only a single letter is allowed", False),("Only a single letter is allowed", False), ("",True), ("",True), ("",True)]
    assert all([hangman.check_cond1(guess[i]) == result[i] for i in range(len(guess)) ])

# Input1:  One letter guesses
    
def test_input2():
    guess_f = [ "a", "b", "c"]
    guess_t = ["d", "e", "f"]
    guess_list = "zaxbvc"
    assert all([hangman.check_cond2(guess_t[i], guess_list) == ("",True) for i in range(len(guess_t)) ])
    assert all([hangman.check_cond2(guess_f[i], guess_list) == ("Already guessed '{}'".format(guess_f[i]), False) for i in range(len(guess_f)) ])

# Input2:  No repetitive guesses

def test_input3():
    guess = [ "1", "?", "n", "o", "f"]
    result=[("Only alphabets are allowed", False),("Only alphabets are allowed", False), ("",True), ("",True), ("",True) ]
    assert all([hangman.check_cond3(guess[i]) == result[i] for i in range(len(guess)) ])

# Input3:  Only alphabets 
      
def test_upper_to_lower():
    guess = [ "A", "B", "C", "d", "e", "f" ]
    result= [ "a", "b", "c", "d", "e", "f"]
    assert all([hangman.upper_to_lower(guess[i]) == result[i] for i in range(len(guess)) ])

# Changes uppercase to lowercase


# D. Test for guess_evaluator

def test_guess_evaluator():
    guess = ["A", "e", "f"]
    guess_list = "zxy"
    result=[("",True), ("",True), ("",True) ]
    assert all([hangman.guess_evaluator(guess[i], guess_list) == result[i] for i in range(len(guess)) ])

# Check for true outputs

def test_guess_evaluator_cond1():
    guess1 = [ "oiu","www","468","zy" ]
    guess_list = "zxy"
    result = ("Only a single letter is allowed", False)
    assert all([hangman.guess_evaluator(guess1[i], guess_list) == result for i in range(len(guess1)) ])

# Check for cond1 outputs

def test_guess_evaluator_cond2():    
    guess2 = [ "x", "z", "y" ]
    guess_list = "xzy"
    assert all([hangman.guess_evaluator(guess2[i], guess_list) == ("Already guessed '{}'".format(guess2[i]), False) for i in range(len(guess2)) ])

# Check for cond2 outputs

def test_guess_evaluator_cond3():
    guess3 = [ "?","1","#" ]
    guess_list = "zxy"
    result = ("Only alphabets are allowed", False)
    assert all([hangman.guess_evaluator(guess3[i], guess_list) == result for i in range(len(guess3)) ])

# Check for cond3 outputs
    
# E. Counting wrong guesses
def test_wrong_guesses():
    words = ["python", "tigers","whales","elephant"]
    guesslist = ["lthwea","qwerty","asdfe","qwdtfe"]
    result =[4, 3, 2, 4]
    assert all([ hangman.wrong_guesses(words[i],guesslist[i]) == result[i] for i in range(len(words)) ])