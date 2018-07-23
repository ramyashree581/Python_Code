import re

pattern = r'Ramya'
sequence = 'Ramya'
if re.match(pattern,sequence):
	print "Match"
else:
	print "Not a match "
r =  re.match(pattern,sequence)		
print r.group()

####################################

print re.search(r'R....', 'Ramya').group() #. macthes one occurence 
print re.search(r'Ra\wy\w', 'RaMya').group() # it mahces a single charachter (Upper case/ Lowercase or '_')
print re.search(r'C\Wke', 'C@ke').group() # it matches special charachters 
print re.search(r'Eat\scake', 'Eat cake').group() #whitepace new line
print re.search(r'Cook\Se', 'Cookie').group() #matches single char
print re.search(r'Eat\tcake', 'Eat	cake').group() #matches a tab
print re.search(r'c\d\dkie', 'c00kie').group() #search digit
print re.search(r'^Eat', 'Eat cake').group() #start 
print re.search(r'cake$', 'Eat cake').group() #end
print re.search(r'Number: [^5]', 'Number: 3').group() #match any charchter except 5

#######################greedy vs non greedy##################

heading  = r'<h1>TITLE</h1>'
print re.match(r'<.*>', heading).group() #Prints everything, is greedy
print re.match(r'<.*?>', heading).group() #? makes it non greedy and prints only first few chatachters possible wil be matcehed
email_address = "Please contact us at: xyz@datacamp.com"
NEW_email_address = re.sub(r'[\w\.-]+@[\w\.-]+', r'ramyashree581@gmail.com', email_address)
print NEW_email_address

pattern = re.compile(r"cookie")
sequence = "Cake and cookie"
print pattern.search(sequence).group()

######################*************************

import re
import requests
the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def get_book(url):
	raw = requests.get(url).text
	start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*",raw ).end()
	stop = re.search(r"II", raw).start()
	text = raw[start:stop]
	return text
def preprocess(sentence): 
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()

book = get_book(the_idiot_url)
processed_book = preprocess(book)
print(processed_book)    









