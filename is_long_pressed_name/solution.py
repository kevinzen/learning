

# [1,1,4,2,1,3]
# Move 4, 1, 3 => [1,1,1,2,3,4]
# pull 1 and put at end of lowest
# 3)

# => create a set
# get counts for each
# create the ideal set
# find the number of changes
# [1,1,4,2,1,3]
# [1,1,1,2,3,4]

from collections import deque
class Solution:

    # For every letter in name
    # if there exists in typed the same letter with at least as many pressed
    # then true


    def is_long_pressed_name(self, name: str, typed: str) -> bool:

        len_n = len(name)
        len_t = len(typed)
        if len_t < len_t:
            return False

        name_q = deque(name)
        typed_q = deque(typed)

        i = 0
        name_letter_counts = {}
        typed_letter_counts = {}

        num_cur_ltr = 0
        cur_ltr = name_q.popleft()
        counter = 1
        while name_q:
            name_letter_counts[str(num_cur_ltr) + cur_ltr] = counter

            next_letter = name_q.popleft()
            if next_letter == cur_ltr:
                counter = counter + 1
            else:
                counter, num_cur_ltr = 1, num_cur_ltr + 1
                cur_ltr = next_letter

        # capture the last letter
        name_letter_counts[str(num_cur_ltr) + cur_ltr] = counter

        # now get counts from typed name
        num_cur_ltr = 0
        cur_ltr = typed_q.popleft()
        counter = 1
        while typed_q:
            typed_letter_counts[str(num_cur_ltr) + cur_ltr] = counter

            next_letter = typed_q.popleft()
            if next_letter == cur_ltr:
                counter = counter + 1
            else:
                counter, num_cur_ltr = 1, num_cur_ltr + 1
                cur_ltr = next_letter

        # capture the last letter
        typed_letter_counts[str(num_cur_ltr) + cur_ltr] = counter

        # must have same letters in each
        if list(name_letter_counts.keys()) != list(typed_letter_counts.keys()):
            return False

        for key in name_letter_counts.keys():
            if typed_letter_counts.get(key) < name_letter_counts[key]:
                return False

        return True








