import unittest

from zigzag_conversion.solution import Solution


class ZigzagConversionTest(unittest.TestCase):

    def test_zigzag_conversion(self):
        s = Solution()

        tests = [
            ("ABCD", 2, "ACBD"),
            ("ABABABABABABABABA", 2, "AAAAAAAAABBBBBBBB"),
            ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
            ('acfimqnjgdbehkorpl', 6 ,'abcdefghijklmnopqr'),
            ('012345678901234567', 6, '001912823737464655'),
            ("", 1, ""),
            ("A", 1, "A"),
            ("AB", 1, "AB")
        ]

        for test in tests:
            input   = test[0]
            numRows = test[1]
            expected = test[2]

            actual = s.zigzag_conversion(input, numRows)
            print("input = " + str(input) + ", actual = " + str(actual) + ", expected = " + str(expected))
            self.assertEqual(expected, actual)
