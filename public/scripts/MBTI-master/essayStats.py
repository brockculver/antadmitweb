import spacy
import os
count =1;
i=0

file1=open(r"C:\Users\brock\antadmitweb\public\scripts\essays.txt","r+")
essays=file1.read();
essays=essays.split("999888999")

while i<count:
    essay = essays[i]
    # print(essay)
    # eori(essay)
    # sori(essay)
    # torf(essay)
    # jorp(essay)
    i=i+1

text = essay
nlp = spacy.load(r"C:\Users\brock\antadmitweb\public\scripts\MBTI-master\mbti model")
doc = nlp(text)
print(doc.cats)
#
# def eori(e):
#
# def sori(e):
#
# def torf(e):
#
# def jorp(e):
