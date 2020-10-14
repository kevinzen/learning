from collections import deque

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        elements = deque(S.split('-'))
        big_str = deque("".join(elements))
        num_letters = len(big_str)

        left_over_count = num_letters % K
        num_sections = num_letters // K

        if left_over_count == 0:
            first_section = False
        else:
            first_section = True

        final_str = deque()
        if first_section:
            first_bite = ''
            for i in range(left_over_count):
                first_bite += big_str.popleft()
                # print("first bite -- " + first_bite)
            final_str.append(first_bite.upper())
            # print("big_str -- " + str(big_str))

        for i in range(num_sections):
            bite = ''
            for i in range(K):
                bite += big_str.popleft()
            bite = bite.upper()
            final_str.append(bite)
            # print("big_str: " + str(big_str))
            # print("bite: " + bite)

        return "-".join(final_str)






