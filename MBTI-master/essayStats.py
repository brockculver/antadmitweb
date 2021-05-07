import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
i=0
count=10
stop_words = set(stopwords.words('english'))
iv=wordnet.synsets('one')[0]
ev=wordnet.synsets('team')[0]
print(iv)
print(ev)
print(iv.wup_similarity(ev))

file1=open(r"C:\Users\brock\antadmitweb\public\scripts\essays.txt","r+")
essays=file1.read();
essays=essays.split("999888999")
print(stop_words)
while i<count:
    essay = essays[i]
    essay=essay.lower()
    i=i+1
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    essay = tokenizer.tokenize(essay)
    essay = [word for word in essay if word not in stop_words]
    # words: list[str] = nltk.word_tokenize(essay)
    fd = nltk.FreqDist(essay)
    print(fd.most_common(8))
    fd1=fd.most_common(10)
    ws=wordnet.synsets(fd1[0][0])
    print(ws)
    try:
        print("extravert comp",ws[0].wup_similarity(ev))
        print("introvert comp",ws[0].wup_similarity(iv))
        if ws[0].wup_similarity(ev)!=ws[0].wup_similarity(iv):
            print("\n!!!!ALERT\n\nALERT\n\nALERT!!!!\n")
    except:
        print("comparison score did not work because no registered synsets")

    # wordsamp=wordnet.synset(fd1.most_common(10)[0][0])
    # print(wordsamp)

# nlp = spacy.load(".\MBTI-Master\mbti model")
# doc = nlp(text)
# print(doc.cats)
#
# def eori(e):
#
# def sori(e):
#
# def torf(e):
#
# def jorp(e):
