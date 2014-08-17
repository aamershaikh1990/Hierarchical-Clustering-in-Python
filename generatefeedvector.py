import re
import feedparser

#Method to get the word counts in each blog 
def getwordcounts(url):
    d = feedparser.parse(url)
    wc = {}

    #for every summary check if there is a summary 
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # For all words in the blog, create a dictionary to count word occurences
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return d.feed.title, wc


def getwords(html):
    # Using a regex splitter, split the words excluding all html tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    #Split by alphanumeric characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    #Return lower case of all words present
    return [word.lower() for word in words if word != '']


apcount = {} #Number of blogs each word appeared
wordcounts = {}
feedlist = [line for line in file('feedlist.txt')]

#read in every line from the feedlist file
for feedurl in feedlist:
    try:
        title, wc = getwordcounts(feedurl) #Get the word counts for each blog
        wordcounts[title] = wc # add to the dictionary

        #Count the number of blogs each word appeared in
        for word, count in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1

        print 'Succeed: %s' % feedurl

    except:
        print 'Failed to parse feeed %s' % feedurl


#Add a lower and upper bound to remove words that are too common/rare
wordlist = []

for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5:
        #Only add the word if it occurs more than 10% and less than 50%
        wordlist.append(w)


#Process for writing out the blogdata matrix 
out = file('blogdata.txt', 'w')
#open the file
out.write('Blog')

#write out all the words
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')

#write out each blog title and score for each word
for blog, wc in wordcounts.items():
    out.write(blog)

    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')