import unittest
import calc
#
#   define the test class
#
class testCalc(unittest.TestCase):

    def setUp(self):
        print '^',
        return
    def tearDown(self):
        print 'v',
        return
        
    def testSimpleAdd(self):
        result,msg = calc.calc(1,'+',1)
        self.assertEqual(result,2.0)

    def testLargeProduct(self):
        result,msg = calc.calc(123456789.0,'*',987654321.0)
        self.assertEqual(result,1.2193263111263526e+17)
    
    def testDivByZero(self):
        result,msg = calc.calc(6,'/',0.0)
        self.assertEqual(msg,'ZeroDivisionError')
#
#   create the test suite
#
TestSuite = unittest.TestSuite()
#
#   add tests to the suite
#
TestSuite.addTest(testCalc("testSimpleAdd"))
TestSuite.addTest(testCalc("testLargeProduct"))
TestSuite.addTest(testCalc("testDivByZero"))
#
#   create the test runner
#
runner = unittest.TextTestRunner()
#
#   execute the tests
#
runner.run(TestSuite)
