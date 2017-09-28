#Caleb Smith-Salzberg, Vivien Lee


import random


def makedictfromtext(file):
    file = open(file,'r')
    plaintext = file.read()
    lines = plaintext.split("\n")
    #delete unnecessary lines from csv file
    del lines[0]
    del lines[len(lines)-1]
    del lines[len(lines)-1]
    
    dict={}
    #adding each line to dictionary
    for line in lines:
        if line[0]=="\"":
            dict[line[0:(line.index("\"",1)+1)]] = line[(line.index("\"",1)+2):]
        else:
            dict[line.split(",")[0]]=line.split(",")[1]
    return dict

def randoc(data):
    '''
    Prints the name of a random weighted occupation

    Arg:
    none

    Ret:
    str name of selected weighted occupation
    Algorithm:
    each occupation from the csv has a certain range of numbers,
    which is the sum of the previous ranges plus the occupation's percentage. 
    '''
    dict = data
    magic =random.randint(0,1000)/10.0
    counter = 0
    for key in dict:
        if (counter + float(dict[key])) - magic > 0:
            return key
        else:
            counter += float(dict[key])


