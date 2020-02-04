import unittest
import Assignment.makeChange as mc

class MakeChangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testName(self):
        #data bounds tests
        self.assertEqual([], mc.makeChange(-1)) #tests out of bounds lower
        self.assertEqual([], mc.makeChange(100.1)) #tests out of bounds upper
        self.assertEqual([], mc.makeChange("hello there")) #test to assure only accept int/float values
        self.assertEqual([], mc.makeChange()) #tests input of nothing
        
        #general use tests
        self.assertEqual([0,0,0,0,0,0,0,0], mc.makeChange(0))
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1))
        self.assertEqual([0,0,0,3,1,0,0,1], mc.makeChange(3.26))
        self.assertEqual([0,0,1,0,0,0,0,0], mc.makeChange(5))
        self.assertEqual([1,1,1,1,1,1,1,1], mc.makeChange(36.41))
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(amount=1))
        
        #rounding tests
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1.001)) #tests rounding down 
        self.assertEqual([0,0,0,1,0,0,0,1], mc.makeChange(1.005)) #tests rounding up to the nearest penny
