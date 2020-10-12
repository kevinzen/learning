
from collections import deque
class Solution:

    def buddyStrings(self, A: str, B: str) -> bool:

        if len(A) != len(B):
            return False

        a_que = deque(A)
        b_que = deque(B)

        diffs = []
        seen = {}

        two_same = False
        last_a = last_b = ""

        while a_que:
            a = a_que.popleft()
            b = b_que.popleft()

            if seen.get(a, None):
                two_same = True
            seen[a] = True

            if a != b:
                diffs.append((a, b))

        if len(diffs) == 0 and two_same:
            return True
        elif len(diffs) == 2 and diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]:
            return True
        else:
            return False








