
import unittest

from collections import deque
from strings_buddy_strings.solution import Solution


class BinaryTreeSerializeDeserializeTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ("", "aa", False),
            ("ab", "ba", True),
            ("aa", "aa", True),
            ("aaaaaaabc", "aaaaaaacb", True),
            ("abcd", "cbad", True),
            ("adce", "aece", False),
            ("abcd", "accb", False),
            ("aaaab", "aaaab", True),
            ("abab", "abab", True),
        ]

        for test in tests:
            A = test[0]
            B = test[1]
            expected = test[2]

            print("A=" + A + " B=" + B)
            actual = s.buddyStrings(A,B)
            print("A=" + A + " B=" + B + " expected = " + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

