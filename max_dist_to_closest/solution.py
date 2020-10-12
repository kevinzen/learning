
# not from end:
# 1 => 1
# 2 => 1
# 3 => 2
# 4 => 2
# 5 => 3
# 6 => 3
# 7 => 4
# n => n // 2 + n % 2
# if end seat then n, else n // 2 + n % 2



from collections import deque
class Solution:

    def max_distance_to_closes(self, seats: []) -> int:

        length = len(seats)
        seats = deque(seats)

        max_dist = 0
        empty_seats = deque()
        first_seat, last_seat = 0, length-1

        for i in range(length):
            if not seats.popleft():
                empty_seats.append(i)
            else:
                empty_this_set = len(empty_seats)
                if empty_this_set != 0:

                    if empty_seats.count(first_seat):
                        max_dist_this_set = empty_this_set
                    else:
                        max_dist_this_set = empty_this_set // 2 + empty_this_set % 2

                    if max_dist_this_set > max_dist:
                        max_dist = max_dist_this_set

                    empty_seats.clear()

        # check to see if the last seat was empty
        empty_this_set = len(empty_seats)
        if empty_this_set != 0:

            if empty_seats.count(last_seat):
                max_dist_this_set = empty_this_set
            else:
                max_dist_this_set = empty_this_set // 2 + empty_this_set % 2

            if max_dist_this_set > max_dist:
                max_dist = max_dist_this_set

        # print(length, empty_seat_count)
        return max_dist




