import unittest

from length_of_longest_substring.solution import Solution


class LengthOfLongestSubstringTest(unittest.TestCase):

    def test_length_of_longest_substring(self):
        s = Solution()
        string1 = 'bbbbba'
        len = s.lengthOfLongestSubstring(string1)
        self.assertEqual(2, len)

        string2 = 'abcabc'
        len = s.lengthOfLongestSubstring(string2)
        self.assertEqual(3, len)

        string3 = "pwwkew"
        len = s.lengthOfLongestSubstring(string3)
        self.assertEqual(3, len)

        string4 = " "
        len = s.lengthOfLongestSubstring(string4)
        self.assertEqual(1, len)

        string5 = "tmmzuxt"
        len = s.lengthOfLongestSubstring(string5)
        self.assertEqual(5, len)

'''

    t - i = 0, seen[v] = None, cur_len = 1, max_len = 1, beg_ptr = 0, seen = {'t': 0 }
    m - i = 1, seen[v] = None, cur_len = 2, max_len = 2, beg_ptr = 0, seen = {'t': 0, 'm': 1 }
    m - i = 2, seen[v] = 1,    cur_len = 1, max_len = 2, beg_ptr = 2, seen = {'t': 0, 'm': 2 }
    z - i = 3, seen[v] = None, cur_len = 2, max_len = 2, beg_ptr = 2, seen = {'t': 0, 'm': 2, 'z': 3 }
    u - i = 4, seen[v] = None, cur_len = 3, max_len = 3, beg_ptr = 2, seen = {'t': 0, 'm': 2, 'z': 3, 'u': 4 }
    x - i = 5, seen[v] = None, cur_len = 4, max_len = 4, beg_ptr = 2, seen = {'t': 0, 'm': 2, 'z': 3, 'u': 4, 'x': 5 }
    t - i = 6, seen[v] = 0,    cur_len = 5, max_len = 5, beg_ptr = 2, seen = {'t': 0, 'm': 2, 'z': 3, 'u': 4, 'x': 5, 't': 6 }

    a - i = 0, seen[v] = None, cur_len = 1, max_len = 1, beg_ptr = 0, seen = {'a': 0 }
    b - i = 1, seen[v] = None, cur_len = 2, max_len = 2, beg_ptr = 0, seen = {'a': 0, 'b': 1 }
    c - i = 2, seen[v] = None, cur_len = 3, max_len = 3, beg_ptr = 0, seen = {'a': 0, 'b': 1, 'c': 2 }
    a - i = 3, seen[v] = 0,    cur_len = 3, max_len = 3, beg_ptr = 1, seen = {'a': 3, 'b': 1, 'c': 2 }
    b - i = 4, seen[v] = 1,    cur_len = 3, max_len = 3, beg_ptr = 2, seen = {'a': 3, 'b': 4, 'c': 2 }
    c - i = 5, seen[v] = 2,    cur_len = 3, max_len = 3, beg_ptr = 3, seen = {'a': 3, 'b': 4, 'c': 5 }
    
    p - i = 0, seen[v] = None, cur_len = 1, max_len = 1, beg_ptr = 0, seen = {'p': 0 }
    w - i = 1, seen[v] = None, cur_len = 2, max_len = 2, beg_ptr = 0, seen = {'p': 0, 'w': 1 }
    w - i = 2, seen[v] = 1,    cur_len = 1, max_len = 2, beg_ptr = 2, seen = {'p': 0, 'w': 2 }
    k - i = 3, seen[v] = None, cur_len = 2, max_len = 2, beg_ptr = 2, seen = {'p': 0, 'w': 2, 'k': 3 }
    e - i = 4, seen[v] = None, cur_len = 3, max_len = 3, beg_ptr = 2, seen = {'p': 0, 'w': 2, 'k': 3, 'e': 4 }
    w - i = 5, seen[v] = 2,    cur_len = 3, max_len = 3, beg_ptr = 3, seen = {'p': 0, 'w': 5, 'k': 3, 'e': 4 }


steps:
    i = counter
    beg_ptr = seen[v] + 1 if seen[v] >= beg_ptr
    cur_len = i - beg_ptr + 1
    max_len = if cur_len > max_len: max_len = cur_len


'''
