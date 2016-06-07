# -*- coding: utf-8 -*-
# lab06Tests.py  by Preston Towers for CS20 lab06,  06/01/2016
# Tests for lab06Funcs.py


import unittest            
from lab06Funcs import *


class TestLab06Functions(unittest.TestCase): 

    # tests for whatMajor

    def test_whatMajor_1(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   whatMajor("PRESTON",students),  "MUSIC" )

    def test_whatMajor_2(self):
        students = [Student("CLAIRE", "GARVAIS", "MUSIC"), Student("PRESTON", "TOWERS", "MUSIC"), Student("TRISTAN", "PEREZ", "MUSIC")]
        self.assertEqual(   whatMajor("PRESTON",students),  "MUSIC" )

    def test_whatMajor_3(self):
        students = [Student("KYLE", "ROATH", "MATH"), Student("TRISTAN", "PEREZ", "MUSIC"),  Student("PRESTON", "TOWERS", "MUSIC")]
        self.assertEqual(   whatMajor("PRESTON",students),  "MUSIC" )

    def test_whatMajor_4(self):
        students = [Student("KYLE", "BUTTS", "POLISCI"), Student("KYLE", "ROATH", "MATH"), Student("CLAIRE", "GARVAIS", "MUSIC")]
        self.assertEqual(   whatMajor("KYLE", students),    "POLISCI")

    def test_whatMajor_5(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("CLAIRE", "GARVAIS", "MUSIC"), Student("KYLE", "ROATH", "MATH")]
        self.assertEqual(   whatMajor("JAKE", students),    False)

    # tests for whatLName

    def test_whatLName_1(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   whatLName("PRESTON", students), "TOWERS")

    def test_whatLName_2(self):
        students = [Student("CLAIRE", "GARVAIS", "MUSIC"), Student("PRESTON", "TOWERS", "MUSIC"), Student("TRISTAN", "PEREZ", "MUSIC")]
        self.assertEqual(   whatLName("PRESTON", students), "TOWERS")

    def test_whatLName_3(self):
        students = [Student("KYLE", "ROATH", "MATH"), Student("TRISTAN", "PEREZ", "MUSIC"),  Student("PRESTON", "TOWERS", "MUSIC")]
        self.assertEqual(   whatLName("PRESTON", students), "TOWERS")

    def test_whatLName_4(self):
        students = [Student("KYLE", "BUTTS", "POLISCI"), Student("KYLE", "ROATH", "MATH"), Student("CLAIRE", "GARVAIS", "MUSIC")]
        self.assertEqual(   whatLName("KYLE", students),    "BUTTS")

    def test_whatLName_5(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("CLAIRE", "GARVAIS", "MUSIC"), Student("KYLE", "ROATH", "MATH")]
        self.assertEqual(   whatLName("JAKE", students),    False)
        
    # tests for countUndec

    def test_countUndec_1(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   countUndec(students), 0)

    def test_countUndec_2(self):
        students = [Student("MORTY", "SMITH", "UNDEC"), Student("RICK", "SANCHEZ", "MECHENGINEERING"), Student("BETH", "SMITH", "BIO")]
        self.assertEqual(   countUndec(students), 1)

    def test_countUndec_3(self):
        students = [Student("MORTY", "SMITH", "UNDEC"), Student("RICK", "SANCHEZ", "MECHENGINEERING"), Student("SUMMER", "SMITH", "UNDEC")]
        self.assertEqual(   countUndec(students), 2)

    def test_countUndec_4(self):
        students = [Student("MORTY", "SMITH", "UNDEC"), Student("MISTER", "MEESEEKS", "UNDEC"), Student("SUMMER", "SMITH", "UNDEC")]
        self.assertEqual(   countUndec(students), 3)


    # tests for lNamesOfUndec

    def test_lNamesOfUndec_1(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   lNamesOfUndec(students), [])

    def test_lNamesOfUndec_2(self):
        students = [Student("MORTY", "SMITH", "UNDEC"), Student("RICK", "SANCHEZ", "MECHENGINEERING"), Student("BETH", "SMITH", "BIO")]
        self.assertEqual(   lNamesOfUndec(students), ["SMITH"])

    def test_lNamesOfUndec_3(self):
        students = [Student("MORTY", "SMITH", "UNDEC"), Student("RICK", "SANCHEZ", "MECHENGINEERING"), Student("SUMMER", "SMITH", "UNDEC")]
        self.assertEqual(   lNamesOfUndec(students), ["SMITH", "SMITH"])

    def test_lNamesOfUndec_4(self):
        students = [Student("MORTY", "SMITH", "UNDEC"), Student("MISTER", "MEESEEKS", "UNDEC"), Student("SUMMER", "SMITH", "UNDEC")]
        self.assertEqual(   lNamesOfUndec(students), ["SMITH", "MEESEEKS", "SMITH"])


    # tests for majorToLNames

    def test_majorToLNames_1(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   majorToLNames("MATH", students), ["ROATH"])

    def test_majorToLNames_2(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   majorToLNames("MUSIC", students), ["TOWERS"])

    def test_majorToLNames_3(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   majorToLNames("THEATER", students), ["HOFFMAN"])

    def test_majorToLNames_4(self):
        students = [Student("CLAIRE", "GARVAIS", "MUSIC"), Student("PRESTON", "TOWERS", "MUSIC"), Student("TRISTAN", "PEREZ", "MUSIC")]
        self.assertEqual(   majorToLNames("MUSIC", students), ["GARVAIS", "TOWERS", "PEREZ"])

    def test_majorToLNames_5(self):
        students = [Student("CLAIRE", "GARVAIS", "MUSIC"), Student("PRESTON", "TOWERS", "MUSIC"), Student("TRISTAN", "PEREZ", "MUSIC")]
        self.assertEqual(   majorToLNames("MATH", students), [])


    # tests for allStudentsMajoringIn

    def test_allStudentsMajoringIn_1(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   allStudentsMajoringIn("MATH", students), [Student(fName="KYLE", lName="ROATH", major="MATH")])

    def test_allStudentsMajoringIn_2(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   allStudentsMajoringIn("MUSIC", students), [Student(fName="PRESTON", lName="TOWERS", major="MUSIC")])

    def test_allStudentsMajoringIn_3(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("KYLE", "ROATH", "MATH"), Student("FLETCHER", "HOFFMAN", "THEATER")]
        self.assertEqual(   allStudentsMajoringIn("THEATER", students), [Student(fName="FLETCHER", lName="HOFFMAN", major="THEATER")])

    def test_allStudentsMajoringIn_4(self):
        students = [Student("CLAIRE", "GARVAIS", "MUSIC"), Student("PRESTON", "TOWERS", "MUSIC"), Student("TRISTAN", "PEREZ", "MUSIC")]
        self.assertEqual(   allStudentsMajoringIn("MUSIC", students), [Student(fName="CLAIRE", lName="GARVAIS", major="MUSIC"), Student(fName="PRESTON", lName="TOWERS", major="MUSIC"), Student(fName="TRISTAN", lName="PEREZ", major="MUSIC")])

    def test_allStudentsMajoringIn_5(self):
        students = [Student("CLAIRE", "GARVAIS", "MUSIC"), Student("PRESTON", "TOWERS", "MUSIC"), Student("TRISTAN", "PEREZ", "MUSIC")]
        self.assertEqual(   allStudentsMajoringIn("MATH", students), [])

    # End of tests for lab06

def runTestsWithPrefix(testFile,prefix):
    """
    run only tests from testFile with a certain prefix
    Example: runTestsWithPrefix("lab03Tests.py","test_isPrimaryColor")
    """
    loader = unittest.TestLoader()
    loader.testMethodPrefix = prefix
    suite = loader.discover('.', pattern = testFile) 
    unittest.TextTestRunner(verbosity=2).run(suite)


# When you run this file, it runs either ALL the tests, or
# just some tests.  It depends on which line you comment out (or not)

if __name__ == '__main__':

    # To run ALL tests, uncomment the "unittest.main(exit=False)" line

    unittest.main(exit=False)  

    # Uncomment "runTestsWithPrefix" line to run just SOME tests
    #    First parameter is name of file with tests
    #    Second parameter is prefix starting with test_ 
    #      such as test_FtoC  or test_isString

    # runTestsWithPrefix("lab06Tests.py","test_lNamesOfUndec") 
