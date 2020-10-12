
from collections import deque
class Solution:

    # 0,1,8 are good numbers
    # 2,5 rotate to 5,2
    # 6,9 rotate to 9,6
    # others are bad

    # first, if number contains 3,4,7 then bad
    # examples:
    # 1, 8, 0 bad alone since they rotate to the same number
    # 2, 5, 6, 9 arr good alone since the rotate to diff numbers
    # rotate in place.

    # 1. if 3, 4, 7 then bad
    # 2. rotate each digit if good digits
    # 3. if int(num) == int(reversed(num)) then bad
    # 4. else good

    def good_numbers(self, N: int) -> int:

        lookups = {
            '0': '0',
            '1': '1',
            '2': '5',
            '3': None,
            '4': None,
            '5': '2',
            '6': '9',
            '7': None,
            '8': '8',
            '9': '6'
        }

        good_numbers = []

        for i in range(1, N+1):
            str_i = str(i)
            exploded = list(str(i))
            rotated = [lookups.get(ele) for ele in exploded]
            if rotated.count(None) > 0:
                continue
            str_r = "".join(rotated)
            # print("num = " + str_i + " rotated = " + "".join(rotated))
            if int("".join(exploded)) != int("".join(rotated)):
                # print("good: " + str_i)
                good_numbers.append(str_i)

        return len(good_numbers)




