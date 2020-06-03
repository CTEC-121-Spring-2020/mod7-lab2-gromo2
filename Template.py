"""
CTEC 121
<Garrett>
<Mod 7 Lab 2>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from math import *
def main():
    '''
    x = 1
    y = 2
    z = 3
    print("x: {0}, y: {1}, z: {2}".format(x, y, z))

    print("pi:", pi, "e:", e)
    print("pi: {0:0.2f}, e: {1:0.2f}".format(pi, e))
    print("pi: {0:10.4f}, e: {1:10.4f}".format(pi, e))
    '''

    # file processing
    print()
    infile = open("sample.txt", 'r')
    print(infile)

    '''
    # get everything
    wholeFileText = infile.read()
    print(wholeFileText)
    wholeFileText = infile.read()
    print("*", wholeFileText, "*", sep= "")

    infile.seek(5)
    wholeFileText = infile.read()
    print("*", wholeFileText, "*", sep= "")
    '''
    '''
    # demo readlines()
    wholeFileTextAsList = infile.readlines()
    print(wholeFileTextAsList)
    for line in wholeFileTextAsList:
        print(line.rstrip())
    '''
    # demo file a line at a time
    for line in infile:
        print(line, end="")

    print()

    line = infile.readline()
    while line != "":       # equivalent to 'while not EOF'
        print(line.rstrip())
        # get next line
        line = infile.readline()

main()    