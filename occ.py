#Caleb Smith-Salzberg, Vivien Lee
#SoftDev1 pd7
#HW5 -- ...and Now Enjoy Its Contents
#2017-09-26

dict={}
file = open('occupations.csv','r')
ugly = file.read()
lines = ugly.split("\n")
import random

#delete unnecessary lines from csv file
del lines[0]
del lines[len(lines)-1]
del lines[len(lines)-1]

#adding each line to dictionary
for line in lines:
    if line[0]=="\"":
        dict[line[0:(line.index("\"",1)+1)]] = line[(line.index("\"",1)+2):]
    else:
        dict[line.split(",")[0]]=line.split(",")[1]

#jobs = []

#for key in dict:
#    jobs.append(key)
#    jobs.append(dict[key])
def randoc():
    '''
    Prints the name of a random weighted occupation
    Arg:
    none
    Ret:
    str name of selected weighted occupation
    '''
    magic =random.randint(0,1000)/10.0
    counter = 0
    for key in dict:
        if (counter + float(dict[key])) - magic > 0:
            return key
        else:
            counter += float(dict[key])

    
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/occupations")
def occ():
    return render_template('template.html', occupation = randoc(), collection = dict)

if (__name__ == "__main__"):
    app.debug = True
    app.run()
