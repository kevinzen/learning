# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def zigzag_conversion(self, s, numRows):

        length = len(s)
        period = 2 * (numRows - 1)

        if len(s) <= (period // 2) + 1 or numRows == 1:
            return s

        extra_steps = length % period
        if extra_steps == 0:
            # ends just before a new peak. not a new peak or valley
            num_peaks = (length // period)
            num_valleys = num_peaks
        elif extra_steps >= 1 and extra_steps < numRows: # a new peak. but not a new valley
            num_peaks = (length // period) + 1
            num_valleys = length // period
        else: # extra_steps >= numRows,  a new peak. AND not a new valley
            num_peaks = (length // period) + 1
            num_valleys = num_peaks

        new = [None]*length
        peaks, valleys = [], []

        index_to_new = 0
        for row in range(numRows-1):

            if row == 0:    #   peaks are all in this row. Figure out valleys now as well.

                for peak_no in range(num_peaks):

                    peak = peak_no * period
                    peaks.append(peak)
                    valley = peak + period // 2
                    valleys.append(valley)  # valley may not exist depending on length, but save anyway for 'mid' processing

                    new[peak_no] = s[peak]  # copy letter for peak

                    if valley <= length - 1:  # if valley is really there, copy that letter too
                        new[length - num_valleys + peak_no] = s[valley]

                    index_to_new = index_to_new + 1 # offset one per peak

            else: # process not-peak/valley rows separately

                if peaks[num_peaks-1] + row < length:  # if true, at least one in the last rank
                    if period * num_peaks - row < length:  # if true, then two in last rank
                        num_in_last_loop = 2
                    else:
                        num_in_last_loop = 1
                else:
                    num_in_last_loop = 0

                num_in_row = 2 * (num_peaks-1) + num_in_last_loop

                done_in_row = 0
                for peak_no in range(num_peaks):

                    valley = valleys[peak_no]

                    if done_in_row < num_in_row:
                        new[index_to_new] = s[valley - period // 2 + row]
                        index_to_new = index_to_new + 1
                        done_in_row = done_in_row + 1

                    if done_in_row < num_in_row:
                        new[index_to_new] = s[valley + period//2 - row]
                        index_to_new = index_to_new + 1
                        done_in_row = done_in_row + 1


        return "".join(new)

        # example:
        # 'PAYPALISHIRING', 'PAHNAPLSIIGYIR'

"""
'PAYPALISHIRING'

P   A   H   N
 A P L S I I G  
  Y   I   R

l = 14, nrows = 3, peaks 4, valleys 3, period = 4

if 14 % 4 > 1
  extra peak
if 14 % 4 >= num_rows
  extra valley

'PAYPALISHIRI'

P   A   H  
 A P L S I I  
  Y   I   R

12 // 4 = 3

Read across the top, it's 'PAHNAPLSIIGYIR'

N = 14 # work length
R = 3  # numRows
i = index in initial word
C = Cycle = 4 = R + 1

I = input = 'PAYPALISHIRING'
Z = zaged = 'PAHNAPLSIIGYIR'

index =
  Z[i=0] = I[i*(R+1)] = I[0 * 4]
  Z[i=1] = I[i*(R+1)] = I[1 * 4]
  Z[i=2] = I[i*(R+1)] = I[2 * 4]
  Z[i=3] = I[i*(R+1)] = I[3 * 4]


Z[0-3] =
I[i]

P   A   H   N
 A P L S I I G
  Y   I   R

PAHNAPLSIIGYIR

    New        Input
P - N[0],      I[0]     =>  0 + 0 * C, pos = 0, n = 0, i = 0   -- top = n
A - N[1],      I[4]     =>  0 + 1 * C, pos = 0, n = 1, i = 1   -- top = n
H - N[2],      I[8]     =>  0 + 2 * C, pos = 0, n = 2, i = 2   -- top = n
N - N[3],      I[12]    =>  0 + 3 * C, pos = 0, n = 3, i = 3   -- top = n
A - N[4],      I[1]     =>  1 + 0 * C, pos = 1, n = 0, i = 4   -- = period + (period - pos) * n
L - N[6],      I[5]     =>  1 + 1 * C, pos = 1, n = 1, i = 6   -- = period + (period - pos) * n
I - N[8],      I[9]     =>  1 + 2 * C, pos = 1, n = 2, i = 8   -- = period + (period - pos) * n
G - N[10],     I[13]    =>  1 + 3 * C, pos = 1, n = 3, i = 10  -- = period + (period - pos) * n
Y - N[11],     I[2]     =>  2 + 0 * C, pos = 2, n = 0, i = 11  -- bot = (length - period + 1) + n = 11
I - N[12],     I[6]     =>  2 + 1 * C, pos = 2, n = 1, i = 12  -- bot = (length - period + 1) + n = 12
R - N[13],     I[10]    =>  2 + 2 * C, pos = 2, n = 2, i = 13  -- bot = (length - period + 1) + n = 13
P - N[5],      I[3]     =>  3 + 0 * C, pos = 3, n = 0, i = 5   -- mid = period + (period - pos) * n = 4 + (4-3) * 0
S - N[7],      I[7]     =>  3 + 1 * C, pos = 3, n = 1, i = 7   -- mid = period + (period - pos) * n = 4 + (4-3) * 1
I - N[9],      I[11]    =>  3 + 2 * C, pos = 3, n = 2, i = 9   -- mid = period + (period - pos) * n = 4 + (4-3) * 2 
0              10
 1            9  11
  2          8    12
    3       7      13   17
      4   6         14 16
        5            15
        
a              b
 c            d  e
  f          g    h
    i       j      k    l
      m   n         o  p
        q             r
        
acfimqnjgdbehkorpl
abcdefghijklmnopqr

a               b
 c            d  e
  f          g    h
    i       j      k    l
      m   n         o  p
        q            r
        
acfimqnjgdbehkorpl
        if length < last_peak + period // 2:
            last_valley = last_peak - period // 2
        else:
            last_valley = last_peak + period // 2

11//2

period = 2 * (numrows - 1)
5 rows = period 8?
1 row, period = 0
2 row, period = 2
3 row, period = 4
4 row, period = 6
5 row, period = 8
6 row, period = 10

peaks = n*period, to end
valley = s[numrows] + n * period, to end
mids:
    for valley in valleys:  # valleys = [5(,15,etc)]
        for i in range(1,numrows-1):
            N[
            




period = 10, rows = 6, n = 11


peaks = 0, period, etc.  # = n * period

valleys = 5, 5 + period, etc





N = len(I) = 14
num_loops = 14/(3+1) # = N/C
extra = N % C # = 14 % 4 = 2

C = numRows + 1      # number in cycle
num_loops, extra_steps = N//C, N % C
for p in range(C):       # p position
    for n in range(num_loops+1):   # n num_loops
        if n <= num_loops and p < extra_steps:        
            N[n] = p * n*C

return N


"""
