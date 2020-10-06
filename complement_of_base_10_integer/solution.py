class Solution(object):

    """
    Input: 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
    Example 2:

    Input: 7
    Output: 0
    Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
    Example 3:

    Input: 10
    Output: 5
    Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

    """

    # for 7:
    # 7 % 2 = 1
    # 7 // 2 = 3
    # 7 = 1* 2^^0 + 1*2^^1 + 1* 2^^2
    # 4 = 0* 2^^0 + 0*2^^1 + 1* 2^^2
    # 10 = 0* 2^^0 + 1*2^^1 + 0 * 2^^2 + 1*2^^3

    # 10 // 1 = 10 % 2 = 0 = (10 // 2**0) % 2
    # 10 // 2 =  5 % 2 = 1 = (10 // 2**1) % 2
    # 10 // 4 =  2 % 2 = 0 = (10 // 2**2) % 2
    # 10 // 8 =  1 % 2 = 1 = (10 // 2**3) % 2

    # 7 // 1 = 7 % 2 = 1
    # 7 // 2 = 3 % 2 = 1
    # 7 // 4 = 1 % 2 = 1
    # 7 // 8 = 0 % 2 = 0

    # 32 // 1 = 32 % 2 = 0
    # 32 // 2 = 16 % 2 = 0
    # 32 // 4 =  8 % 2 = 0
    # 32 // 8 =  4 % 2 = 0
    # 32 // 16 = 2 % 2 = 0
    # 32 // 32 = 1 % 2 = 1

    def complement(self, N: int) -> int:

        exp = ret_val =  0
        complements = [1,0]
        while (True):

            order_val = 2**exp
            num = N // order_val

            complement = complements[num % 2]
            ret_val = ret_val + complement * order_val

            if num < 2:
                break
            exp = exp + 1

        return ret_val
