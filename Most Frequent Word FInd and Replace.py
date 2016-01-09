__author__ = 'SONY'

from nltk.corpus import gutenberg as gb
from nltk.corpus import brown as bw
from nltk.tokenize import sent_tokenize as st
from nltk import tokenize
import re

def si(s1,s2):
    l1= 0
    l2 = 0
    for s in s1.lower():
        l1+= ord(s)
    for s in s2.lower():
        l2+= ord(s)

    return l1==l2
    

def compare(sent1, sent2):
    s1 = re.findall(r"\w+",str(sent1))
    s2 = re.findall(r"\w+",str(sent2))
    ans = 0
    for w1 in set(s1):
        for w2 in set(s2):
            if(si(w1,w2)):
                ans+=1

    m = len(s1)/20 + len(s2)/20
    if m == 0:
        return 0
    return ans/m

#print(gb.fileids())
parents = gb.raw("edgeworth-parents.txt")
outputfile = open(r'C:\Users\SONY\SkyDrive\output_from_NLP.02','w')

parents = r"\n\n"+parents+r"\n\n"
parents = re.sub(r'\r|"|( ){2,}',r'',parents)
paras = re.findall(r"\n\n(.*?)\n\n",parents,re.DOTALL)
#print(paras[:5])
parasnew = []
sents = [[] for _ in paras]
i = 0
for s in paras:
    s = re.sub(r"\n"," ",s)
    ns = s.split(".")
    if(len(ns)>1):
        sents[i]+=ns
        parasnew.append(ns)
    else:
        sents[i]+=[s]
        parasnew.append(ns)
    i+=1
    #print(st(s))
i=0
allsent = [s for j in range(len(sents)) for s in sents[j] if s!='']
#print(len(sents),print(len(sents[0])))

util = [[0 for _ in range(5500)] for _ in range(5500)]

for index in range(len(allsent)):
    print(index)
    for com in range(index+1,min(len(allsent),index+100)):
        #print(allsent[index],allsent[com])
        util[index][com] = compare(allsent[index],allsent[com])
        util[com][index] = util[index][com]

print (max([max(util[i]) for i in range(len(util))]))

raw_output = ""
utilIndex = 0

for i in parasnew:
    maxs = 1
    parano = 0
    mastr = ""
    masumu = 0
    for s in i:
        if(parano<maxs):
            sumu = sum(util[utilIndex])

            #print(sumu)
            if(sumu>.02 and masumu<sumu):
                masumu = sumu
                mastr = s


    raw_output+=''.join(mastr)
    outputfile.write("".join(mastr))
    outputfile.write(".\n")
    raw_output+=r'\n'
    parano+=1
    utilIndex+=1
    print(utilIndex)
print(raw_output)
print(len(raw_output))
print(len(parents))
print("The percentage compression is",len(raw_output)*100.0/len(parents))

outputfile.close()
