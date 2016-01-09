# Robin Camille Davis
# CODEX 2016

import nltk
from nltk.corpus import gutenberg as gb


#print(gb.fileids())
par = gb.raw("edgeworth-parents.txt")
parshort = par[:10000]

#Tokenize
partok = nltk.word_tokenize(parshort)

#Tag POS
partag = nltk.pos_tag(partok)

#Outputs POS-tagged text
print(nltk.ne_chunk(partag, binary=False))

##Output:
##  managed/VBN
##  by/IN
##  a/DT
##  (PERSON Mr./NNP Hopkins/NNP)
##  ,/,
##  an/DT
##  agent/NN
