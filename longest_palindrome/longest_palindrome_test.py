import unittest

from longest_palindrome.solution import Solution


class LongestPalindromeTest(unittest.TestCase):

    def test_longest_palindrome(self):
        s = Solution()
        # len = s.longest_palindrome(string1)
        # self.assertEqual(5, len)
        #

        string1 = 'bbbbba'
        max_pally = s.longest_palindrome(string1)
        self.assertEqual('bbbbb', max_pally)

        string2 = 'abcabc'
        max_pally = s.longest_palindrome(string2)
        self.assertEqual('a', max_pally)

        string3 = "aaababaqq"
        max_pally = s.longest_palindrome(string3)
        self.assertEqual('ababa', max_pally)

        string4 = "asdfggfdsa"
        max_pally = s.longest_palindrome(string4)
        self.assertEqual('asdfggfdsa', max_pally)

        string5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        answer = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        max_pally = s.longest_palindrome(string5)
        self.assertEqual(answer, max_pally)

'''

'babaa' - answer = 'aba'
    b - i = 0, other 'b' at 3
    in reverse order:
        3 - bab MATCH!, longest = 3
    
    a - i = 1, other 'a's at 3,4
    in reverse order:
        4 - no
        3 - aba MATCH!, len = 3, not longer
         
    b - i = 3, no others
    
    a - i = 4. len to end = 2, don't bother looking since < 3
        
pseudocode:
    loop through string:
        - get all letters with > one occurence
        - create set of indexes to letters with one or more occurence
        
    - while length from i to end of string > largest pal:
        for each letter that has dups:
            start with furthest and work to closest:
                if MATCH, palindrome -- save that length and stop
    

data_structure for 'babaa'
{
    'a': [1, 3, 4]
    'b': [0, 2]    
}

for all keys in struct:
    compare furthest to closest, if match then calc len and stop
    
    



'asdsa' - answer = 'asdsa'
    a - i = 0, other 'a' at '5', reverse between and MATCH, longest so done

'aaababaqq' - answer = 'ababa'
    a - i = 0, other 'a's at 1, 2, 4, 6
    in reverse order:
        6 - no
        4 - no
        2 - MATCH!, stop

    a - i = 1, others at 2, 4, 6
    in reverse order:
        6 - no
        4 - no
        2 - MATCH!, stop -- but 'aaa' is longer.

    a - i = 2, others at 4, 6
    in reverse order:
        6 - MATCH!, stop. new longer
    
    b - i = 3, other at 5
    in reverse order:
        5 - MATCH!, stop. len = 3

'''
