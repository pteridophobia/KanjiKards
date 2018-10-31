# KanjiKards
Kanji flash cards program (python)
This program will be flashcards for all 2136 of the Jouyou Kanji
(A complete list of them can be found at http://nihongo.monash.edu/jouyoukanji.html)
The goal for the applicartion is to help people memorize and learn kanji.
Some features that will be implemented to help achive this goal are: 
  1) A visual dictionary of all the kanji where the user can look through and click on an individual 
  kanji and see the japanese reading, romanji(english letters that spell the japanese reading), 
  english meanings (there may be several meanings to each kanji), and the grade level that the kanji is learned in.
  2) The ability to make sets of kanji. Some premade sets will be included. Some of which will be the kanji sorted into
  the grade levels that they are leaned in Japan.
  3) A practice mode where users can drill themselves on sets of kanji. This mode will have three modes:
  a mode where the user sees the kanji character and tries to remember the meaning and reading, a mode where the user
  sees the japanese reading and tries to remember the meaning and kanji character, and a mode where the user sees the
  english meaning or meanings and tries to remmebr the Japaese reading and kanji character. Once the user thinks they
  remmeber the information they click the show answer button. They then press a button to indicate whether they remembered
  right or not(This is how the anki software does their flash cards).
  4) Algorithms that track the users number of right and wrong answers for each kanji and adjust the frequency that each
  kanji appears in the practice modes
  5) A feature that lets the user reset all data that tracks their right and wrong answers
  6) A feature that inks to the website jisho.org(This is the same site that will be used for html scrapping) for the kanji 
  that the user wants to know more information about. 
  7) A cumulative daily practice mode that gradually adds more kanji each day. The user will use this mode once a day
  with a percentage of the kanji that have already been added to the mode. If the user misses a day then the old kanji that
  they were supposed to review will be added to the ext day's review. The new kanji that would have been added, however, will 
  not be added in order to not overwhelm the user with too many new kanji in one day. 

The 2136 kanji will be added into a doubly linked list of type class KanjiKard. The kanji will be scrapped from 
the website jisho.org which is an online Japanese dictionary. Beautiful Soup is a tool that will be used to help
with the scrapping. Once all the kanji has been scrapped and loaded into the linked list a function will write all
the contents of the list to a .json or .txt file. Then when the program is started it will read from the .txt/.json 
file and load the linked list. This is to prevent the program form requireing a internet conection and will also have
a quicker run time than if web scrapping was done every time the program starts up. User data will be saved in the same 
file to make loading simplier. If the user want a reset on their stats then a backup file containing the list of kanji 
and default values for user data will be loaded and be used to overwrite the save file. The user created and premade sets
of kanji will be saved in a third .txt/.json file. Since the list won't have a variabe name for each kanji in the list
the file that includes the sets will only contain the kanji characters that the set contains. When reading in a set 
the kanji character from the set file will be read and then the list will be searched for the memner that contains that
character. 
