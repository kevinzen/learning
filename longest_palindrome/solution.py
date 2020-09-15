# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) in [0,1]:
            return s

        max_len = 1
        max_pally = s[0]

        # create count array first
        letters_and_positions = {}
        length = len(s)
        for i,v in enumerate(s):
            if letters_and_positions.get(v, None) == None:
                letters_and_positions[v] = [i]
            else:
                letters_and_positions[v].append(i)

        # now identify all letters with only one occurance:
        one_occ_letters = []
        for letter, positions in letters_and_positions.items():
            if len(positions) == 1:
                one_occ_letters.append(letter)

        # note: if only one letter with a single occurrence, a palindrome can cross that letter.
        # otherwise, palindromes can only occur across substrings that contain one of these letters, and it has to
        # be in the middle --- eg, 'aabaaaaaaaaa' contains 'aabaa' and 'aaaaaaaaa', 'aaaaaaaa', 'aaaaaaa', etc.
        # it is possible to break into substrings that contain only one or zero single letters.

        # 'aadbadaaca' has two letters with single occurrence, 'b' and 'c'. substrings that have one or zero are:
        # 'aa', 'aad', 'aadbadaa', 'aabaa', 'aba', 'aaa', 'aaaa' 'aca'
        # 'yzmadamimadamyzaaaaaaaaaaaaaaaaaaaaax':
        #  - 'i' is only single letter. start there and work out: 'mim', 'amima', etc.
        #  - largest blocks with a single letter appearing in the middle are:
        #  - 'yzmadamimadamyz', 'aaaaaaaaaaaaaaaaaaaaax'
        # if we can isolate these substrings first, then we can figure it out.
        # so, first start with only single letters and work out.
        # after that, break into substrings containing none of those letters. reduces to:
        # 1. start with 'i' and work out. find 'madamimadam', then 'x' and get nothing.
        # 2. do 'yzmadam', and 'madamyzaaaaaaaaaaaaaaaaaaaaa'





        for letter, positions in letters_and_positions.items():
            if len(positions) > 1:
                reversed_positions = list(reversed(positions))
                for position in positions:
                    for rev_pos in reversed_positions:
                        if position >= rev_pos and (rev_pos - position) < max_len:
                            # print("done")
                            break
                        else:
                            frag = s[position:rev_pos+1]
                            # print(s, position, rev_pos, frag, frag[::-1])
                            if frag == frag[::-1]:
                                if len(frag) > max_len:
                                    # print(frag, " is pally!")
                                    max_len = len(frag)
                                    max_pally = frag


        return max_pally

"""
data_structure for 'babaa'
{
    'a': [(1,4) (3,2), (4,1)],
    'b': [(0,5) (2,3)]  
}

for all keys in struct:
    compare furthest to closest, if match then calc len and stop
    
"""

