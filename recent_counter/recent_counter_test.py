import unittest

from recent_counter.solution import RecentCounter, RecentCounterDeque


class RecentCounterTest(unittest.TestCase):

    def test_recent_counter(self):

        tests = [
            ([1, 100, 3001, 3002], [1, 2, 3, 3])
        ]


        for test in tests:

            pings = test[0]
            counts = test[1]

            print("pings = " + str(pings) + " counts = " + str(counts))

            counter = RecentCounter()
            counter_deque = RecentCounterDeque()
            for i in range(len(pings)):
                count = counter.ping(pings[i])
                count_deque = counter_deque.ping(pings[i])
                print("Sorted_list: ping = " + str(pings[i]) + " count = " + str(count) + " expected cpount = " + str(counts[i]))
                print("Deque:       ping = " + str(pings[i]) + " count_deque = " + str(count_deque) + " expected cpount = " + str(counts[i]))
                self.assertTrue(counts[i], count)


