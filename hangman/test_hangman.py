import os
from re import T

import hangman

def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_mask_word_single_letter():
    secret_word="elephant"
    guesses=["l"]
    ret = hangman.mask_word(secret_word,guesses)
    assert ret == "-l------"

def test_mask_word_double_letter():
    secret_word="elephant"
    guesses=["e"]
    ret = hangman.mask_word(secret_word,guesses)
    assert ret == "e-e-----"

def test_mask_word_bad_guess():
    secret_word="elephant"
    guesses=["x"]
    ret = hangman.mask_word(secret_word,guesses)
    assert ret == "--------"

def test_mask_word_good_guess_mix():
    secret_word="elephant"
    guesses=["x","e","h"]
    ret = hangman.mask_word(secret_word,guesses)
    assert ret == "e-e-h---"
   




def test_create_status_normal():
    secret_word = "elephant"
    guesses = ["a", "x", "h"]
    remaining_turns = 7
    assert hangman.create_status(secret_word, guesses, remaining_turns) == """Word: ----ha--
Guesses: a x h
Remaining turns : 7
"""

def test_create_status_no_guesses():
    secret_word = "elephant"
    guesses = []
    remaining_turns = 8
    assert hangman.create_status(secret_word, guesses, remaining_turns) == """Word: --------
Guesses: 
Remaining turns : 8
"""

def test_play_round_correct_guess():
    secret_word = "elephant"
    guesses = []
    remaining_turns = 8
    new_guess = "e"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, new_guess, remaining_turns)
    assert guesses == ["e"]
    assert remaining_turns == 8
    assert repeat == False
    assert finished == False


def test_play_round_correct_wrong():
    secret_word = "elephant"
    guesses = ["e"]
    new_guess = "x"
    remaining_turns = 7
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, new_guess, remaining_turns)
    assert guesses == ["e", "x"]
    assert remaining_turns == 6
    assert repeat == False
    assert finished == False



def test_play_round_correct_repeat():
    secret_word = "elephant"
    guesses = ["e"]
    remaining_turns = 8
    new_guess = "e"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, new_guess, remaining_turns)
    assert guesses == ["e"]
    assert remaining_turns == 8
    assert repeat == True
    assert finished == False


def test_play_round_correct_complete():
    secret_word = "elephant"
    guesses = ["e","l","p","h","a","n","t"]
    remaining_turns = 8
    new_guess = "t" 
    remaining_turns,repeat, finished = hangman.play_round(secret_word, guesses, new_guess, remaining_turns)
    assert finished == True


