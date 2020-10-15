
from collections import deque
from sortedcontainers.sortedset import SortedSet
class Solution:

    def minMeetingRooms(self, intervals: [[int]]) -> int:
        if len(intervals) == 0:
            return 0

        meetings_hash = {}
        for meeting_request in intervals:
            meetings_hash.setdefault(meeting_request[0], []).append(meeting_request[1])

        start_times = list(meetings_hash.keys())
        start_times.sort()
        starts = deque(start_times)
        end_times = deque()
        rooms_needed_times = []

        while starts:
            mtg_start = starts.popleft()
            end_times.extend(meetings_hash[mtg_start])
            # print("end_times = " + str(end_times))
            rooms_needed_at_this_time = 0
            meetings_that_go_later_than_mtg_start = deque()
            while end_times:
                end_time = end_times.popleft()
                if end_time > mtg_start:
                    rooms_needed_at_this_time += 1
                    meetings_that_go_later_than_mtg_start.append(end_time)

            rooms_needed_times.append(rooms_needed_at_this_time)
            end_times = meetings_that_go_later_than_mtg_start

        return max(rooms_needed_times)



    def minMeetingRooms_brute(self, intervals: [[int]]) -> int:

        if len(intervals) == 0:
            return 0
        num_mtgs = len(intervals)

        big_sched = {}
        for i in range(num_mtgs):
            start = intervals[i][0]
            end = intervals[i][1]
            for j in range(start, end):
                if big_sched.get(j, None) == None:
                    big_sched[j] = 1
                else:
                    big_sched[j] = big_sched[j] + 1

        mtg_counts = big_sched.values()
        return max(mtg_counts)

