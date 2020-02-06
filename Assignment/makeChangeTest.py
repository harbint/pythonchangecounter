import unittest
import Assignment.makeChange as mc

class MakeChangeTest(unittest.TestCase):
# Analysis
#    makeChange(amount)
#
#    inputs:
#        amount: integer/float, 100>= amount >= 0, mandatory, unvalidated
#
#    outputs:
#        side-effects: no state change
#        returns: array: array with values dependent on value of amount
#                    {[0,0,0,0,0,0,0,0] , []}
#
#    confidence level: BVA
#
# Happy path
#    test 010: nominal value of amount 0 low bound test
#                result: [0,0,0,0,0,0,0,0]
#    test 020: nominal value of amount 99.99 high bound test
#                result: [4,1,1,4,3,2,0,4]
#    test 030: nominal value of amount that is represented by one value in the output array: 1
#                result: [0,0,0,1,0,0,0,0]
#    test 040: nominal value of amount that is represented by multiple values in the output array: 36.41
#                result: [1,1,1,1,1,1,1,1]
#    test 050: nominal value of amount that is represented by multiple of the same value in the output array: 3.26
#                result: [0,0,0,3,1,0,0,1]
#    test 060: nominal value of amount that tests rounding down functionality: 1.001
#                result: [0,0,0,1,0,0,0,0]
#    test 070: nominal value of amount that tests rounding up functionality: 1.005
#                results: [0,0,0,1,0,0,0,1]
# Sad path
#    test 910: non-integer value of amount: "hello there"
#                result: []
#    test 920: non-integer value of amount: 
#                result: []
#    test 930: below bounds test of negative integer amount: -1
#                result: []
#    test 940: above bounds test of integer amount: 100.1
#                result: []
#    test 950: abnormal passing of assignment statement amount: amount=1
#                result: [0,0,0,1,0,0,0,0]
#
#    Happy Path tests
    def test010_ShouldTestNominalLowBound(self):
        self.assertEqual([0,0,0,0,0,0,0,0], mc.makeChange(0))

    def test020_ShouldTestNominalHighBound(self):
        self.assertEqual([4,1,1,4,3,2,0,4], mc.makeChange(99.99))

    def test030_ShouldTestNominalOneValue(self):
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1))

    def test040_ShouldTestNominalMultipleValues(self):
        self.assertEqual([1,1,1,1,1,1,1,1], mc.makeChange(36.41))

    def test050_ShouldTestNominalMultipleOfOneValue(self):
        self.assertEqual([0,0,0,3,1,0,0,1], mc.makeChange(3.26))

    def test060_ShouldTestNominalRoundDown(self):
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1.001))

    def test070_ShouldTestNominalRoundUp(self):
        self.assertEqual([0,0,0,1,0,0,0,1], mc.makeChange(1.005))

#    Sad Path tests

    def test910_ShouldTestBadInputTypeString(self):
        self.assertEqual([], mc.makeChange("hello there"))

    def test920_ShouldTestBadInputTypeNull(self):
        self.assertEqual([], mc.makeChange())

    def test930_ShouldTestOutOfBoundsNegative(self):
        self.assertEqual([], mc.makeChange(-1))

    def test940_ShouldTestOutOfBoundsUpper(self):
        self.assertEqual([], mc.makeChange(100.1))

    def test950_ShouldTestAbnormalAssignment(self):
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(amount=1))
        