# Robin Camille Davis
# CODEX 2016

import nltk
from nltk import word_tokenize as tok
from nltk import pos_tag as postag
from nltk import ne_chunk as ne
from nltk.corpus import gutenberg as gb
from collections import Counter

#print(gb.fileids())
par = gb.raw("edgeworth-parents.txt")
parshort = par[:10000]

#Tokenize
partok = tok(parshort)

#Tag POS
partag = postag(partok)

#Outputs POS-tagged text
parne = ne(partag, binary=False)

chars = []
for n in parne:
    if type(n) == nltk.tree.Tree:
        if n.label() == 'PERSON':
            for m in n:
                chars.append(m[0])

words_to_count = (word for word in chars if word[:1].isupper())
c = Counter(words_to_count)
print c

##Output:
#Counter({u'Mary': 26, u'Peggy': 4, u'Mr.': 4, u'Annie': 3, u'Hopkins': 3, u'Edmund': 2, u'Nancy': 2, u'Isabella': 1, u'Harvey': 1, u'Navan': 1, u'Miss': 1, u'Maud': 1, u'Edgeworth': 1, u'Maria': 1})
