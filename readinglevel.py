# Checks every line in a file to see if it contains at least one lower-case letter,
# and returns each line that does with the whitespace removed
def getBook(file):
    L = ' '.join( [str(line.rstrip()) for line in open(file) if any(c.islower() for c in line)] )
    return(L)
    file.close()
    
# Uses re.sub function to replace all punctuation and all('s) from the text with
# an empty string and to replace all '!' and '?' with '.'
def cleanup(text):
    import re
    text = re.sub("--", '', text)
    text = re.sub('-', ' ', text)
    text = re.sub("'s", '', text)
    text = re.sub('["()\'_/\,:;]', '', text)
    return(re.sub('[!?]', '.', text))

# Uses .lower() to lowercase all of the characters in the text and removes
# all non-letter characters from the text using the re.sub function. Then, the function
# returns a list containing each word in the text
def extractWords(text):
    import re
    text = text.lower()
    text = re.sub(r'[^\w\s]','',text)
    return(list(text.split()))

# Returns all of the sentences in the text by splitting them by '. ',
# but since the last element in the list would be empty, it is removed
def extractSentences(text):
    return( [sent for sent in (text+' ').split('. ')][:-1] )

# If the first letter in the word contains a vowel, it adds one to the syllable-count
# list. Then for every letter that contains a vowel and comes after a non-vowel letter,
# the functions adds one to the syllable-count
def countSyllables(word):
    count = 0
    if word[0] in 'aeiou':
        count = count + 1
    for i in range(len(word)-1):
        if word[i] in 'aeiou' and word[i-1] not in 'aeiou':
            count = count + 1
    return(count)

# The two variables, cpw and wps, are assigned to the average number of characters per word
# and average number of words per sentence, respectively. Then the variables are used to calculate
# the Automated Readability Score. This function calls on previous functions.
def ars(text):
    cpw = sum([len(c) for c in extractWords(text)]) / len(extractWords(text))
    wps = len(extractWords(text)) / len(extractSentences(text))
    return((4.71*cpw)+(.5*wps)-21.43)

# The two variables, wps and spw, are assigned to the average number of words per sentence
# and average number syllables per word, respectively. Then the variables are used to calculate
# the Flesch-Kincaid Index. This function calls on previous functions.
def fki(text):
    wps = len(extractWords(text)) / len(extractSentences(text))
    spw = sum([ countSyllables(c) for c in extractWords(text) ]) / len(extractWords(text))
    return((.39*wps)+(11.8*spw)-15.59)

# The two variables, cphw and sphw, are assigned to the average number of characters per 100 words
# and average number of sentences per 100 words, respectively. Then the variables are used to calculate
# the Coleman-Liau Index. This function calls on previous functions.
def cli(text):
    cphw = sum([len(c) for c in extractWords(text)]) / (len(extractWords(text)) / 100)
    sphw = len(extractSentences(text)) / (len(extractWords(text)) / 100)
    return((.0588*cphw)-(.296*sphw)-15.8)

# Reads in a book from a file and evaluates its readability. Returns
# None.
def evalBook(file):
    text = cleanup(getBook(file))
    print("Evaluating {}:".format(file.upper()))
    print("  {:5.2f} Automated Readability Score".format(ars(text)))
    print("  {:5.2f} Flesch-Kincaid Index".format(fki(text)))
    print("  {:5.2f} Coleman-Liau Index".format(cli(text)))
