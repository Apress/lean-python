
#
#   Unit tests for Story 94 Feature: "Calculator"
#

import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator.calculator("The calculator")
        
    def tearDown(self):
        self.calculator.dispose()
        self.calculator = None

        
            def testPerformCalculation0001(self):
        self.calculator.runTest('','','')
        self.assertEqual(str(self.calculator.result),"Ending")

    def testPerformCalculation0002(self):
        self.calculator.runTest('1','','')
        self.assertEqual(str(self.calculator.result),"Ending")

    def testPerformCalculation0003(self):
        self.calculator.runTest('1','+','')
        self.assertEqual(str(self.calculator.result),"Ending")

    def testPerformCalculation0004(self):
        self.calculator.runTest('abc','+','1')
        self.assertEqual(str(self.calculator.result),"A is not a number")

    def testPerformCalculation0005(self):
        self.calculator.runTest('1','+','pqr')
        self.assertEqual(str(self.calculator.result),"B is not a number")

    def testPerformCalculation0006(self):
        self.calculator.runTest('1','x','1')
        self.assertEqual(str(self.calculator.result),"Invalid operator")

    def testPerformCalculation0007(self):
        self.calculator.runTest('-1,000,000,000.000001','+','1')
        self.assertEqual(str(self.calculator.result),"A out of range")

    def testPerformCalculation0008(self):
        self.calculator.runTest('1000000000.000001','+','1')
        self.assertEqual(str(self.calculator.result),"A out of range")

    def testPerformCalculation0009(self):
        self.calculator.runTest('1','+','-1000000O00.000001')
        self.assertEqual(str(self.calculator.result),"B out of range")

    def testPerformCalculation0010(self):
        self.calculator.runTest('1','+','1000000000.000001')
        self.assertEqual(str(self.calculator.result),"B out of range")

    def testPerformCalculation0011(self):
        self.calculator.runTest('-1000000000.00000','+','-1000000000.00000')
        self.assertEqual(str(self.calculator.result),"-2000000000.0")

    def testPerformCalculation0012(self):
        self.calculator.runTest('1000000000.00000','+','1000000000.00000')
        self.assertEqual(str(self.calculator.result),"2000000000.0")

    def testPerformCalculation0013(self):
        self.calculator.runTest('1','-','1')
        self.assertEqual(str(self.calculator.result),"0.0")

    def testPerformCalculation0014(self):
        self.calculator.runTest('1','*','1')
        self.assertEqual(str(self.calculator.result),"1.0")

    def testPerformCalculation0015(self):
        self.calculator.runTest('1','/','1')
        self.assertEqual(str(self.calculator.result),"1.0")

calculatorTestSuite = unittest.TestSuite()

calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0001"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0002"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0003"))
"""
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0004"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0005"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0006"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0007"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0008"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0009"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0010"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0011"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0012"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0013"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0014"))
calculatorTestSuite.addTest(CalculatorTestCase("testPerformCalculation0015"))"""

runner = unittest.TextTestRunner()
runner.run(calculatorTestSuite)
