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



def hiragana_to_romanji(hira):
    romanji = str()
    str1 = ['']*(len(hira))
    i = 0
    next_rep = -1
    def hiragana_dict(hira):
        return {
            'あ': 'a',
            'い': 'i',
            'う': 'u',
            'え': 'e',
            'お': 'o',
            'か': 'ka',
            'き': 'ki',
            'く': 'ku',
            'け': 'ke',
            'こ': 'ko',
            'さ': 'sa',
            'し': 'shi',
            'す': 'su',
            'せ': 'se',
            'そ': 'so',
            'た': 'ta',
            'ち': 'chi',
            'つ': 'tsu',
            'て': 'te',
            'と': 'to',
            'な': 'na',
            'に': 'ni',
            'ぬ': 'nu',
            'ね': 'ne',
            'の': 'no',
            'は': 'ha',
            'ひ': 'hi',
            'ふ': 'fu',
            'へ': 'he',
            'ほ': 'ho',
            'ま': 'ma',
            'み': 'mi',
            'む': 'mu',
            'め': 'me',
            'も': 'mo',
            'や': 'ya',
            'ゆ': 'yu',
            'よ': 'yo',
            'ら': 'ra', 
            'り': 'ri',
            'る': 'ru',
            'れ': 're',
            'ろ': 'ro',
            'わ': 'wa',
            'ゐ': 'wi',
            'ゑ': 'we',
            'を': 'wo',
            'ん': 'n',
            'が': 'ga',
            'ぎ': 'gi',
            'ぐ': 'gu',
            'げ': 'ge',
            'ご': 'go',
            'ざ': 'za',
            'じ': 'ji',
            'ず': 'zu',
            'ぜ': 'ze',
            'ぞ': 'zo',
            'だ': 'da',
            'ぢ': 'dji',
            'づ': 'dzu',
            'で': 'de',
            'ど': 'do',
            'ば': 'ba',
            'び': 'bi',
            'ぶ': 'bu',
            'べ': 'be',
            'ぼ': 'bo',
            'ぱ': 'pa',
            'ぴ': 'pi',
            'ぷ': 'ぷ',
            'ぺ': 'pe',
            'ぽ': 'po',
            'きゃ': 'kya',
            'きゅ': 'kyu',
            'きょ': 'kyo',
            'しゃ': 'sha',
            'しゅ': 'shu',
            'しょ': 'sho',
            'ちゃ': 'cha',
            'ちゅ': 'chu',
            'ちょ': 'cho',
            'にゃ': 'nya',
            'にゅ': 'nyu',
            'にょ': 'nyo',
            'ひゃ': 'hya',
            'ひゅ': 'hyu',
            'ひょ': 'hyo',
            'みゃ': 'mya',
            'みゅ': 'myu',
            'みょ': 'myo',
            'りゃ': 'rya',
            'りゅ': 'ryu',
            'りょ': 'ryo',
            'ぎゃ': 'gya',
            'ぎゅ': 'gyu',
            'ぎょ': 'gyo',
            'じゃ': 'ja',
            'じゅ': 'ju',
            'じょ': 'jo',
            'ぢゃ': 'ja',
            'ぢゅ': 'ju',
            'ぢょ': 'jo',
            'びゃ': 'bya',
            'びゅ': 'byu',
            'びょ': 'byo',
            'ぴゃ': 'pya',
            'ぴゅ': 'pyu',
            'ぴょ': 'pyo',
            'ょ': '',
            'ゅ': '', 
            'ゃ': '',
            'っ': '',
            '\n': ''
        }[hira]
    for c in hira:
        str1[i] = c
        if c == 'ょ' or c == 'ゅ' or c == 'ゃ':
            str1[i-1] = str1[i-1] + str1[i]
        i += 1
    i = 0
    for h in str1:
        if h == 'っ':
            next_rep = 1
        romanji = romanji + hiragana_dict(str1[i])
        if next_rep == 1:
            next_rep = 0
            temp = hiragana_dict(str1[i+1])[0:1]
            romanji = romanji + hiragana_dict(str1[i+1])[0:1] + hiragana_dict(str1[i])
        i+=1
    return romanji
print(hiragana_to_romanji("はっぴゃっく"))


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
one = KanjiKard() # This is the head to the list of KanjiKard s
one.kanji = "一"
one.reading = "いち"
one.romanji = "ichi"
one.english = "one" 
one.english2 = ""
one.english3 = ""
one.grade_level = 1
one.next = KanjiKard()
head = KanjiKard()
head = one
temp = KanjiKard()
temp = head
count = 0
after = KanjiKard()
while count < 3:
    
    if count == 0:
        after.kanji = "十"
        after.reading = "じゅう"
        after.romanji = "juu"
        after.english = "ten"
        after.grade_level = 1
    elif count == 1:
        after.kanji = "七"
        after.reading = "asf"
        after.romanji = "nana"
        after.english = "seven"
        after.grade_level = 1
    elif count == 2:
        after.kanji = "五"
    #print(after.kanji)
    after.prev = temp
    temp.next = after
    temp = after
    after.next = KanjiKard()
    after = after.next
    count += 1



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

def search_for_kanji(head, target): #searches list for target kanji and returns pointer to that KanjiKard
    temp = KanjiKard()
    temp = head
    temp_kanji = temp.kanji
    while temp_kanji != None:
        if temp.next == None:
            print(target, "could not be found")
            break
        if temp_kanji == target:
            print("Found", target)
            return temp;
        temp = temp.next
        temp_kanji = temp.kanji
testS = KanjiKard()
testS = search_for_kanji(head, target = "七")
print(testS.kanji, ":Search test")


print("now we print all kanji\n")
print_all_kanji(head)





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