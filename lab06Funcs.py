# lab06Funcs.py by Preston Towers for CS20 lab06, 06/01/2016
# Writing to files Python

from collections import namedtuple
Student = namedtuple("Student","fName lName major")



def lineToStudent(inputLine):
   """
   creates a Student (named tuple) from an inputLine (string)
   >>> lineToStudent('SHARON, ROBINSON, PHYSICS')
   Student(fName='SHARON', lName='ROBINSON', major='PHYSICS')
   >>> 
   """

   itemStripped = inputLine.strip()  # remove the newlines
   itemSplit = itemStripped.split(',')  # split into a list at the comma

   # now, itemSplit[0] is the first name,
   #      itemSplit[1] is the last name
   #      itemSplit[2] is the major
   # but each might still have spaces

   return Student(itemSplit[0].strip(), itemSplit[1].strip(), itemSplit[2].strip())


def Main():
    infile = open('students.txt', 'r')
    inputList = [] # empty list of all lines in file

    # read all lines from file into inputList

    for line in infile:
        inputList = inputList + [line]

    # Now inputList is a list of strings. 

    # make variable students "global" so it is 
    # available at Python prompt, and 
    # initialize to empty list

    global students 
    students = [] 

    # make a list of students from the inputList

    for item in inputList:
        thisStudent =  lineToStudent(item)
        students = students + [thisStudent]

    # end of Main()

if __name__ == "__main__":
    Main()


def whatMajor(fName, listOfStudents):
    """
    return the major of first student in listOfStudents with first name fName, False if none found

    >>> whatMajor("FRED",[Student("MARY","KAY","MATH"), Student("FRED","CRUZ","HISTORY"), Student("CHRIS","GAUCHO","UNDEC")])
    'HISTORY'
    >>> 
    """
    listOfMajors = ""
    for i in range(len(listOfStudents)):

       # step through every item in listOfStudents
       # when you find a match, return that students's major

       if listOfStudents[i].fName == fName:
          listOfMajors += listOfStudents[i].major
       listOfMajors.split()

    # if you got all the way through the loop and didn't find
    #  the name, return False
    if listOfMajors == "":
       return False
    else:
       return listOfMajors
       
