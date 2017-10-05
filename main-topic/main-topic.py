
import re
import nltk

with open('titles') as f:
    content = f.read()

titles = content.splitlines()
lemma = nltk.stem.wordnet.WordNetLemmatizer()
f = {}
for title in titles:
    words = re.findall('[\w]+', title)
    for word in words:
        w = lemma.lemmatize(word.lower())
        if not w in f:
            f[w] = set()
        f[w].add(title)

s = list(f.iteritems())
s.sort(lambda x, y: len(x[1]) - len(y[1]), None, True)

for x in s:
    if len(x[0]) > 3:
        print '%-3d\t%s' % (len(x[1]), x[0])

