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

    def test_whatMajor_4(self):
        students = [Student("KYLE", "BUTTS", "POLISCI"), Student("KYLE", "ROATH", "MATH"), Student("CLAIRE", "GARVAIS", "MUSIC")]
        self.assertEqual( whatMajor("KYLE", students), "POLISCI" "MATH")

    def test_whatMajor_5(self):
        students = [Student("PRESTON", "TOWERS", "MUSIC"), Student("CLAIRE", "GARVAIS", "MUSIC"), Student("KYLE", "ROATH", "MATH")]
        self.assertEqual( whatMajor("JAKE", students), False)

    # tests for whatLName

    def test_whatLName_1(self):
        self.assertEqual()

    def test_whatLName_2(self):
        self.assertEqual()

    def test_whatLName_3(self):
        self.assertEqual()

    def test_whatLName_4(self):
        self.assertEqual()

    def test_whatLName_5(self):
        self.assertEqual()
        
    # tests for countUndec

    def test_countUndec_1(self):
        self.assertEqual()

    def test_countUndec_2(self):
        self.assertEqual()

    def test_countUndec_3(self):
        self.assertEqual()

    def test_countUndec_4(self):
        self.assertEqual()

    def test_countUndec_5(self):
        self.assertEqual()

    # tests for lNamesOfUndec

    def test_lNamesOfUndec_1(self):
        self.assertEqual()

    def test_lNamesOfUndec_2(self):
        self.assertEqual()

    def test_lNamesOfUndec_3(self):
        self.assertEqual()

    def test_lNamesOfUndec_4(self):
        self.assertEqual()

    def test_lNamesOfUndec_5(self):
        self.assertEqual()

    # tests for majorToLNames

    def test_majorToLNames_1(self):
        self.assertEqual()

    def test_majorToLNames_2(self):
        self.assertEqual()

    def test_majorToLNames_3(self):
        self.assertEqual()

    def test_majorToLNames_4(self):
        self.assertEqual()

    def test_majorToLNames_5(self):
        self.assertEqual()

    # tests for allStudentsMajoringIn

    def test_allStudentsMajoringIn_1(self):
        self.assertEqual()

    def test_allStudentsMajoringIn_2(self):
        self.assertEqual()

    def test_allStudentsMajoringIn_3(self):
        self.assertEqual()

    def test_allStudentsMajoringIn_4(self):
        self.assertEqual()

    def test_allStudentsMajoringIn_5(self):
        self.assertEqual()

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

    # unittest.main(exit=False)  

    # Uncomment "runTestsWithPrefix" line to run just SOME tests
    #    First parameter is name of file with tests
    #    Second parameter is prefix starting with test_ 
    #      such as test_FtoC  or test_isString

    runTestsWithPrefix("lab06Tests.py","test_whatMajor") 
