#Caleb Smith-Salzberg, Vivien Lee
#SoftDev1 pd7
#HW5 -- ...and Now Enjoy Its Contents
#2017-09-26
from util.jobs import makedictfromtext, randoc    
from flask import Flask, render_template

app = Flask(__name__)

jobdict = makedictfromtext("data/occupations.csv")

@app.route("/occupations")
def occ():
    return render_template('template.html', occupation = randoc(jobdict), collection = jobdict )

if (__name__ == "__main__"):
    app.debug = True
    app.run()
