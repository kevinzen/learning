# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = {}
        begin_ptr = 0
        max_len = 0
        for i,v in enumerate(s):

            last_seen = seen.get(v, None)
            if last_seen != None  and last_seen >= begin_ptr:
                begin_ptr = seen.get(v) + 1

            cur_len = i - begin_ptr + 1

            if max_len < cur_len:
                max_len = cur_len

            seen[v]=i # save the latest index for this letter

        return max_len


# note:
#  -- did not see to reset beginning index after first sighting
#  -- did not try no duplicate letters
#  -- need to try simple cases first, then go to advanced.






