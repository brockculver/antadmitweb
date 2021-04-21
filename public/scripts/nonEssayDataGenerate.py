import names
import random as r
import numpy as np
from numpy import random
data=[]
count = 600;
degrees=["business","education","health","engineering","art","communications","history","natural science"]
states=["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

i=0
file1=open(r"C:\Users\brock\antadmitweb\public\scripts\essays.txt","r+")
essays=file1.read();
essays=essays.split("999888999")

while i<count:
    #makes the essay for the student
    essay = essays[i]
    # assigns gender
    j=r.randint(0,1)
    if j==0:
        gend='male'
    else:
        gend='female'

    # assigns sport attribute
    sport="-"
    if (r.randint(0,99)<15) and (gend=='male'):
        whichsport=r.randint(0,335)
        if whichsport<61:
            sport="baseball"
        elif whichsport<92:
            sport="basketball"
        elif whichsport<110:
            sport="XC"
        elif whichsport<203:
            sport="Football"
        elif whichsport<213:
            sport="golf"
        elif whichsport<217:
            sport="ice hockey"
        elif whichsport<233:
            sport="lacrosse"
        elif whichsport<268:
            sport="soccer"
        elif whichsport<278:
            sport="swimming"
        elif whichsport<284:
            sport="tennis"
        elif whichsport<319:
            sport="track and field"
        elif whichsport<323:
            sport="volleyball"
        elif whichsport<336:
            sport="wrestling"


    if r.randint(0,99)<15 and gend=='female':
        whichsport=r.randint(0,222)
        if whichsport<27:
            sport="basketball"
        elif whichsport<45:
            sport="XC"
        elif whichsport<50:
            sport="field hockey"
        elif whichsport<56:
            sport="golf"
        elif whichsport<70:
            sport="lacrosse"
        elif whichsport<109:
            sport="soccer"
        elif whichsport<142:
            sport="softball"
        elif whichsport<155:
            sport="swimming"
        elif whichsport<162:
            sport="tennis"
        elif whichsport<196:
            sport="track and field"
        elif whichsport<223:
            sport="volleyball"

    country="USA"
    state=states[r.randint(0,49)]
    town="-"

    racenum=r.randint(1,1000)
    if racenum<=610:
        race="white"
    elif racenum<790:
        race="hispanic"
    elif racenum<=913:
        race="black"
    elif racenum<=960:
        race="asian"
    elif racenum<=980:
        race="multiple"
    else:
        race="native american"
    # random creation of age
    age=18
    age+=round(np.random.normal(.3,.7))
    if r.randint(0,10)==1:
        age=21+r.randint(0,48)
    if r.randint(0,500)==1:
        age=12+r.randint(0,4)

    # ranom degree selection
    degree=degrees[r.randint(0,len(degrees)-1)]

    # sat generation using average 1050, varying act slightly
    sat=round(np.random.normal(105,10))*10

    if sat>1600:
        sat=1600
    if sat<400:
        sat=400

    if sat>1300:
        act=round(sat/45)
    elif sat>1100:
        act=round(sat/48)
    elif sat>800:
        act=round(sat/55)
    elif sat>=400:
        act=round(sat/60)

    actvariance=round(np.random.normal(0,1))
    act=act+actvariance

    if act>36:
        act=36

    gpa=np.random.normal(3.3,.4)

    if sat>1100:
        gpa+=.15
    if sat>1300:
        gpa+=.1
    if sat<1000:
        gpa-=.15
    if sat<800:
        gpa-=.1
    if gpa>4:
        gpa-=.3
    if gpa>4:
        gpa=4
    gpa=round(gpa,2)
    gpaw=round(gpa+gpa*.05*np.random.normal(1,.15)*r.randint(0,1),2)

    data=data+[[names.get_full_name(gender=gend), gend, sat, act, gpa, gpaw, degree, age, race, country, town, state, sport,"-",essay]]
    i=i+1
print(data)

file2=open(r"C:\Users\brock\antadmitweb\public\scripts\studentInputData.txt","w+")
for student in data:
    for item in student:
        file2.write(str(item))
        if(len(str(item))<=30):
            file2.write(",")
    file2.write("\n")
