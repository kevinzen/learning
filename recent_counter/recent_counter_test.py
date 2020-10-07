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

    def test_max_integer(self):

        def solution(numbers: [int]) -> int:
            length = len(numbers)
            if length == 0:
                return 0

            result = numbers[0]
            for i in range(1, length):
                if numbers[i] > result:
                    result = numbers[i]

            return result

        r = solution([0,1,1,1,4,5,6,-1])
        self.assertEqual(6,r)

        r = solution([-100,1,1,1,4,5,6,100])
        self.assertEqual(100,r)

        r = solution([])
        self.assertEqual(0,r)

        r = solution([-1, -1, -3, -5, -2])
        self.assertEqual(-1,r)

        r = solution([0,1,1,999,4,5,6,-1])
        self.assertEqual(999,r)



