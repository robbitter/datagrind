import string
#insert text file name
fname = 'text file'
fhand = open(fname)
alpha = dict()
alphalist = list()
charcount = 0
for line in fhand:
    #cleaning up text, removing punctuation, all lower case, etc.
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    wordlist = line.split()
    #isolating characters
    for word in wordlist:
        charlist = list(word)
        #compiling letters in dictionary
        for char in charlist:
            alpha[char] = alpha.get(char,0)+1
            #total characters for averages
            charcount += 1

# list for sorting
for char, num in alpha.items():
    alphalist.append((num,char))

alphalist.sort(reverse=True)

for value, key in alphalist:
    #cleaning up the float/percentage
    avg = round(((value/charcount)*100),4)
    msg ='The character '+str(key)+' was found in the text '+str(value)+ ' times, representing a usage rate of '+str(avg) + '%'
    print(msg)
