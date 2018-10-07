#TODO: add all 2136 kanji to KanjiKard class
#TODO: create a basic UI
#TODO: allow user to make sets of cards 
#TODO: make a practice mode that allows users to practice sets ok cards
#TODO: make algorithms to help determine how often and which cards show up in practice
#TODO: let user browse all kanji
#TODO: allow user to save data locally
#TODO: make load function to read saved local data
#TODO: make a search function that allows user to search by multiple different elements
#TODO: impliment an optional timer for practice mode
#TODO: make links to jishoo.org for further imformation regarding specific kanji
#TODO: other stuff

import struct
from struct import *

class KanjiKard:
    """The class for KanjiKards"""
    kanji = ""      # The kanji character
    reading = ""    # The hiragana reading of character
    romanji = ""    # The romanji (english alphabet) reading
    english = ""    # The english meaning of the character
    english2 = ""   # Other meanings
    english3 = ""   # Other meanings
    grade_level = 1 # The grade level for which the character is learned
    num_attempts = 0# The number of attempts the user has used for the character
    num_right = 0   # The number of correct attempts
    num_wrong = 0   # The number of incorrect attempts
      
    def __init__(self):
        self.next = None# pointer to next
        self.prev = None# pointer to previous
"""
 = KanjiKard()



.kanji = ""
.reading = ""
.romanji = ""
.english = ""
.english2 = ""
.english3 = ""
.grade_level = 1
.next = 
.prev = 
"""
#num_attempts, num_right, and num_wrong should always be initialized to 0 unless user data is loaded
#now we add all 2,136 Jōyō kanji:
#the primary english meaning will be used as the var name 
#if there are multiple kanji with the same primary english meanning then meaning_reading will be used instead
#where the reading is romanji

#declarations for all kards in grade 1
#done before setting elements so .next pointers are valid in compile
one = KanjiKard()
two = KanjiKard()
three = KanjiKard()
four = KanjiKard()
five = KanjiKard()
six = KanjiKard()
seven = KanjiKard()
eight = KanjiKard()
nine = KanjiKard()
ten = KanjiKard()
under = KanjiKard()

one.kanji = "一"
one.reading = "いち"
one.romanji = "ichi"
one.english = "one" 
one.english2 = ""
one.english3 = ""
one.grade_level = 1
one.next = two

two.kanji = "二"
two.reading = "に"
two.romanji = "ni"
two.english = "two"
two.english2 = ""
two.english3 = ""
two.grade_level = 1
two.next = three
two.prev = one

three.kanji = "三"
three.reading = "さん"
three.romanji = "san"
three.english = "three"
three.english2 = ""
three.english3 = ""
three.grade_level = 1
three.next = four
three.prev = two

four.kanji = "四"
four.reading = "よん"
four.romanji = "yon"
four.english = "four"
four.english2 = ""
four.english3 = ""
four.grade_level = 1
four.next = five
four.prev = three

five.kanji = "五"
five.reading = "ご"
five.romanji = "go"
five.english = "five"
five.english2 = ""
five.english3 = ""
five.grade_level = 1
five.next = six
five.prev = four

six.kanji = "六"
six.reading = "ろく"
six.romanji = "roku"
six.english = "six"
six.english2 = ""
six.english3 = ""
six.grade_level = 1
six.next = seven 
six.prev = five

seven.kanji = "七"
seven.reading = "しち　/　なな"
seven.romanji = "shichi / nana"
seven.english = "seven"
seven.english2 = ""
seven.english3 = ""
seven.grade_level = 1
seven.next = eight
seven.prev = six

eight.kanji = "八"
eight.reading = "はち"
eight.romanji = "hachi"
eight.english = "eight"
eight.english2 = ""
eight.english3 = ""
eight.grade_level = 1
eight.next = nine
eight.prev = seven

nine.kanji = "九"
nine.reading = "きゅう"
nine.romanji = "kyuu"
nine.english = "nine"
nine.english2 = ""
nine.english3 = ""
nine.grade_level = 1
nine.next = ten
nine.prev = eight


ten.kanji = "十"
ten.reading = "じゅう"
ten.romanji = "juu"
ten.english = "ten"
ten.english2 = ""
ten.english3 = ""
ten.grade_level = 1
ten.next = under
ten.prev = nine 


   

temp = KanjiKard()
temp = one
temp_kanji = temp.kanji
while temp_kanji != None: #prints out each kanji, reading,  and english meaning
    if temp.next == None:
        break
    print(temp.kanji,":", temp.reading, ":", temp.english )
    temp = temp.next
    temp_kanji = temp.kanji





