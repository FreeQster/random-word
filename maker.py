import random

words = []
i = 0
j = 0

with open('src/wordlist.txt') as my_file:
    for line in my_file:
        words.append(line)
        i = i+1

with open('src/de-2048-v1.txt') as my_file:
    for line in my_file:
        words.append(line)
        i = i+1

#print(i,"words read")
length = input("How many words do we want? (Zahl)  ")

output = ""

while j < int(length):
    rnd = random.randrange(0,i)
    #print(words[rnd])
    #output = output + words[rnd]
    output = ''.join((output, words[rnd]))
    j = j+1

print(output.replace('\n', ' '))
