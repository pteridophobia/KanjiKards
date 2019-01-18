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
#TODO: use html scrubbing to load all kanji
#TODO: implement function to take all loaded kanji[] and put them into the KanjiKard class
#TODO: implement functions to traverse and search the doubly linked list of the KanjiKard class
import re
import struct
from struct import *
from bs4 import BeautifulSoup

import re
import struct
from struct import *


class KanjiKard:
    """The class for KanjiKards"""
    kanji = ""      # The kanji character
    reading = ""    # The hiragana reading of character
    romanji = ""    # The romanji (english alphabet) reading
    english = ""    # The english meaning of the character
    grade_level = 1 # The grade level for which the character is learned
    num_attempts = 0# The number of attempts the user has used for the character
    num_right = 0   # The number of correct attempts
    num_wrong = 0   # The number of incorrect attempts
    daily_correct = 0
    daily_wrong = 0
    daily_easy = 0
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
.daily_correct = 0
.daily_wrong = 0
.daily_easy = 0
.next = 
.prev = 
"""
#num_attempts, num_right, and num_wrong should always be initialized to 0 unless user data is loaded


head = KanjiKard() # This is the head to the list of KanjiKards 
head.kanji = '頭'
head.english = 'head'
head.grade_level = 2
head.reading = 'あたま'
head.romanji = 'atama'
head.next = KanjiKard()

temp = KanjiKard()
temp = head
count = 0
after = KanjiKard()

kanji_file = open("KanjiKard_list_V1.txt", "r")
i = 0
it = 0
for line in kanji_file:
    kanji_in = line
    kanji_in = kanji_in[0:len(kanji_in)-1]
    if line == '\n':
        print("New line")
    elif line == None:
        print("None")
    elif it == 0:
        after.kanji = kanji_in
       # print(after.kanji)
        it += 1
    elif it == 1:
        after.reading = kanji_in
        #print(after.reading)
        it += 1
    elif it == 2:
        after.romanji = kanji_in
        #print(after.romanji)
        it += 1
    elif it == 3:
        after.english = kanji_in
        #print(after.english)
        it += 1
    elif it == 4:
        if kanji_in == 9:
            after.grade_level = "taught in junior high"
            #print(after.grade_level)
            it += 1
        else:
            after.grade_level = kanji_in
            #print(after.grade_level)
            it += 1
    elif it == 5:
        it = 0
        after.prev = temp
        temp.next = after
        temp = after
        after.next = KanjiKard()
        after = after.next
    i+=1

print(i)

def print_all(head): #prints all members of each KanjiKard
    temp = KanjiKard()
    temp = head
    temp_kanji = temp.kanji
    while temp_kanji != None: 
        if temp.next == None:
            break
        print(temp.kanji,":", temp.reading, ":", temp.english )
        temp = temp.next
        temp_kanji = temp.kanji

def print_all_kanji(head): #prints only the kanji for each KanjiKard
    temp = KanjiKard()
    temp = head
    temp_kanji = temp.kanji
    while temp_kanji != None: 
        if temp.next == None:
            break
        print(temp.kanji)
        temp = temp.next
        temp_kanji = temp.kanji
"""
def search_for_kanji(head): #searches list for target kanji and returns pointer to that KanjiKard
    print("Enter the kanji you want to search for: ")
    target = input()
    temp = KanjiKard()
    temp = head
    temp_kanji = temp.kanji
    while temp_kanji != None:
        if temp.next == None:
            print(target, "could not be found")
            break
        if temp_kanji == target:
            print("Found", target)
            print("\n")
            print(temp.kanji,":", temp.reading, ":", temp.english )
            return temp
        temp = temp.next
        temp_kanji = temp.kanji
"""


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def search(head): #searches list for target kanji and returns pointer to that KanjiKard
    print("Enter the romanji spelling, English word, hiraganna/katakanna, or kanji character for the kanji you want to search for: ")
    target = input()
    temp = KanjiKard()
    temp = head
    temp_kanji = temp.kanji
    num_found = 0
    while temp_kanji != None:
        if temp.next == None:
            if num_found == 0:
                print(target, "could not be found")
            else:
                print(target, "found", num_found, "times")
            break
        if temp.romanji == target or temp.english == target or temp.kanji == target or temp.reading == target or findWholeWord(target)(temp.english):
            print("Found", target)
            print(temp.kanji,":", temp.reading, ":", temp.romanji, ":", temp.english )
            print('\n')
            num_found += 1
            #return temp

        temp = temp.next
        temp_kanji = temp.kanji

#testS = KanjiKard()
#testS = search_for_kanji(head, target = "七")
#if testS != None:
#    print(testS.kanji, ":Search test")
running = 1
def end(Q):
    global running
    running = 0
actions = {
    '1': print_all_kanji,
    '2': print_all,
    '3': search,
    'q': end
}
while(running):
    print("Welcome\n")
    print("Available actions:\n")
    print("1.) display all kanji\n")
    print("2.) display all kanji : readings : meaning\n")
    print("3.) search for kanji\n")
    print("q.) quit\n")
    print("Enter the number of the action you wish to execute: ")

    action = input()
    
    actions[action](head)
#print_all_kanji(head)





"""
Turn
ing in "final" code that produces debugging output is bad form, and points may be deducted if you 
have extensive debugging output. We suggest you the following: 
o
Near the top of your program write a debug function that can be turned on and off by changing 
a 
single variable. For example,
debugging = True
def
debug(*s): 
if
debugging: 
print
(*s)
o
Where you want to produce debugging output use
:
debug(”This is my debugging output”)
instead of 
print
. 
o
(
How it works
: Using * in front of the parameter of a 
function means that a
variable number 
of arguments can be passed to that parameter. Then using *s as print
’
s
argument passes 
along those arguments to print.)

"""