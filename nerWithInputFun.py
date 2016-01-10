#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Robin Camille Davis
# CODEX 2016

# Top 5 names from a .txt file

##This script asks for the URL to a plain-text file (Project Gutenberg).
##It outputs the top 5 person names from the text using the
##Stanford Named Entity Recognition interface in NLTK.
##
##Caveats: first/last names and honorifics not considered


import urllib2
import re
from nltk import tree
from nltk import word_tokenize as tok
from nltk import pos_tag as postag
from nltk import ne_chunk as ne
from nltk.corpus import gutenberg as gb
from collections import Counter
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")


partition = 10000 #set to -1 for whole file

def returnNames(url):
        
    theurl = "http://www.ccel.org/ccel/bible/kjv.txt"
    #raw_input("URL to .txt file: ")
    sourcefile = urllib2.urlopen(theurl)
    source = sourcefile.read()
    
    #Tokenize
    sourcetok = tok(source[:partition])
    
    #Tag POS
    sourcetag = postag(sourcetok)
    
    #Outputs POS-tagged text
    sourcene = ne(sourcetag, binary=False)
    
    charsall = []
    for n in sourcene:
        if type(n) == tree.Tree:
            if n.label() == 'PERSON':
                for m in n:
                    charsall.append(m[0])
    
    honorifics = ['Mr.', 'Mrs.', 'Ms.', 'Miss', 'Dr.', 'Prof.', 'Professor', 'Lord', 'Lady', 'Sir', 'Madam', 'Dame', 'Rev.', 'Rabbi']
    
    charsallnames = []
    for s in charsall:
        if s in honorifics:
            pass
        else:
            charsallnames.append(s)
    
    counted = (word for word in charsallnames if word[:1].isupper())
    c = Counter(counted)
    charscommon = c.most_common(5)
    
    chars = []
    for s in charscommon:
        chars.append(s[0])
    
    print '\nMost common names:'
    print '\t'.join(chars)
    return chars,source 

#locfolder = r'C:\Users\SONY\SkyDrive\\'
locfolder = ""
locx = "20 books from gutenberg - Sheet1.csv"

with open(locfolder+locx,'r') as f:
    rows=[L.strip().split(",") for L in f]

##for r in rows:
##    for ri in r:
##        print ri  #page 1, input needs to be selected
##    print    



#index = int(raw_input("Enter the selected Book index ")) #selected i/p
def selecttext(index):
    data = rows[index+2]
    return data[0]


#print data[0],  #page 2 book title

def printnames():
    name,src = returnNames(data[2]) #data[2] is the url to be fetched
    print name  #page 2, input to be typed in
    data.append(name)

##    print data #print everything except src
##    newTitle = raw_input(" Rename the Book ") #page 3
##    auth = data[1]
##    print (newTitle," by ", auth) #page 4 top

def selectnames():

    newNames = []
    namesOfPpl = data[3] #d[3] is the names col
    for n in namesOfPpl: 
        nn = raw_input("Enter the New Name for "+n)
        newNames.append(nn)

    print "Featuring "

def outputfile():
    OutputFile = src
    for i in range(5):
        print newNames[i]," as : ",namesOfPpl[i] #page 4 complete
        OutputFile = re.sub(namesOfPpl[i],newNames[i],OutputFile)


    Out = open(newTitle+".txt",'w') #page 5
    Out.write(OutputFile)
    Out.close()

    print "Done"
