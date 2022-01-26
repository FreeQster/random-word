#Import
import random
import os


#Define vars
words = []
i = 0
j = 0

scd = (os.path.dirname(__file__))

#English wordlist to array
with open(scd+'/src/wordlist.txt') as my_file:
    for line in my_file:
        words.append(line)
        i = i+1
#German wordlist to array
with open(scd+'/src/de-2048-v1.txt') as my_file:
    for line in my_file:
        words.append(line)
        i = i+1

#Ask for number of words input
length = input("How many words do we want? (Number)  ")

output = ""

#Roll words and add to var output
while j < int(length):
    rnd = random.randrange(0,i)
    output = ''.join((output, words[rnd]))
    j = j+1

#Output without line breaks
print(output.replace('\n', ' '))
