import unittest

from split_string_max_unique_substrings.solution import Solution


class SplitStringMaxUniqueSubstringsTest(unittest.TestCase):

    def test_aplit_stringa(self):
        s = Solution()


        tests = [
            # ("a", ['a'], 1),
            # ("aba", ['ab', 'a'], 2),
            # ("aa", ['aa'], 1),
            # ("aaa", ['aa', 'a'], 2),
            # ("abcabc", ['a', 'b', 'cab', 'b'], 4),
            # ("abcabcabc", ['a', 'b', 'cab', 'ca', 'bc' ], 6),
            # ("a", 1),
            # ("ab", 2),
            # ("abc", 3),
            # ("abca",3),
            # ("abcab",4),
            # ("abcabc", 4),
            # ("abcabca", 5),
            # ("abcabcab", 5),
            # ("aabbcc", 4),
            # ("aabbcca", 5),
            # ("aabbccaa", 5),
            # ("abcabcabc",  6),
            # ("abcabcabcabc", 7),
            ("aaaxyzaaaabcd", 9),
            ("abcdefghijklmnop", 16),
        ]

        for test in tests:
            input   = test[0]
            expected_result = test[1]

            # print("UNIQUE_WORDS input = " + input + ", expected_result = " + str(expected_result) + ", num_words = " + str(num_words_in_result))
            actual = s.maxUniqueSplit(input)
            print("UNIQUE_WORDS input = " + input + ", actual = " + str(actual) + " num words = " + str(expected_result))
            self.assertEqual(expected_result, actual)

# 'abcdefghijklmnop' => 'a b c d e f g h i j k l m n o p'
# 'abcdefghijklmnop' => 'a b c d e f g h i j k l m n o p'
# 'abcdefghijklmnop' => 'a b c d e f g h i j k l m n o p'
# 'abcdefghijklmnop' => 'a b c d e f g h i j k l m n o p'
