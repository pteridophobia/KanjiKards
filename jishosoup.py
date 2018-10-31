from bs4 import UnicodeDammit
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
markup = '<a href="http://jisho.org">'#I linked to <i>jisho.org</i></a>'
soup = BeautifulSoup(markup)
soup.prettify()
# '<html>\n <head>\n </head>\n <body>\n  <a href="http://example.com/">\n...'

print(soup.prettify())

dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
dammit.original_encoding

h1 = http.client.HTTPConnection('https://jisho.org/')
print(h1)

html_doc = "https://jisho.org/"
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())