import sys
if (len(sys.argv) < 4):
    print('Usage: python3 bypass.py <word_to_insert> <position_to_insert> <wordlist>')
    sys.exit()

word = sys.argv[1]
positionWord = int(sys.argv[2])
originalWordlist = sys.argv[3]

# Read the wordlist
wordlist = open(originalWordlist)
wordlistReaded = wordlist.read()

#Convert the string to list
def Convert(string):
    li = list(string.split("\n"))
    return li

list = Convert(wordlistReaded)
list.pop()

howIncrease = len(list) + (len(list)//(positionWord-1))
lenList = len(list)
position = range(positionWord - 1, howIncrease, positionWord)

for number in position:
    list.insert(number, word)

modifiedWordlist = '\n'.join(list)

newWordlist = open('newWordlist.txt', 'w')
newWordlist.write(modifiedWordlist)
newWordlist.close()
