#Caleb Smith-Salzberg, Vivien Lee
#SoftDev1 pd7
#HW5 -- ...and Now Enjoy Its Contents
#2017-09-26
    
from flask import Flask, render_template
import util.jobs
app = Flask(__name__)

@app.route("/occupations")
def occ():
    return render_template('template.html', occupation = jobs.randoc(makedictfromtext("data/occupations.csv")), collection = makedictfromtext("data/occupations.csv"))

if (__name__ == "__main__"):
    app.debug = True
    app.run()
