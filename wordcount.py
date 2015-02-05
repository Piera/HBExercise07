from sys import argv
import string

script, filename = argv

f = open(filename)

words = {}
excludes = set(string.punctuation)
#print excludes

for line in f:
    line = line.replace("--", " ")
    line = line.lower().rstrip().split()

    # line = ["as", "you--well"]
    # for word in line:
    #     word = word.replace("--", " ")
    #     print word

    # line = ['as', 'you', 'well']

    #iterate through each line list
    for word in line:
        #print "old:", word
        
        for character in word:
            if character in excludes:
                word = word.replace(character,"")
        #print "new", word
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

# sort by alphabet, then frequency
print sorted(sorted(words.items()), key = lambda x: x[1], reverse = True)

# sort by frequency, then alphabet
# print sorted(sorted(words.items(), key = lambda x: x[1]))

# print words


# for k, v in sorted(words.items(), key = lambda x: x[1], reverse = True):
#     print k, v