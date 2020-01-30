import unittest
import Assignment.makeChange as mc

class MakeChangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testName(self):
        self.assertEqual([0,0,0,0,0,0,0,0], mc.makeChange(0))
        
        self.assertEqual([], mc.makeChange(-1)) #tests out of bounds lower
        self.assertEqual([], mc.makeChange(100.1)) #tests out of bounds upper
        
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1))
        
        self.assertEqual([0,0,0,0,1,0,0,1], mc.makeChange(.256)) #tests rounding up to the nearest penny
        #self.assertEqual([1,0,0,0,0,0,0,0], mc.makeChange(20.001)) #tests rounding down 
        
        self.assertEqual([], mc.makeChange("hello there")) #test to assure only accept int/float values
