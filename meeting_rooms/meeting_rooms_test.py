
import unittest

from meeting_rooms.solution import Solution


class MeetingRoomsTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()

        tests = [
            ( [[0, 30],[5, 10],[15, 20]], 2),
            ([[7,10],[2,4]], 1),
            ([], 0),
            ([[1, 5], [8, 9], [8, 9]], 2),
            ([[9, 10], [4, 9], [4, 17]], 2)
        ]

        for test in tests:
            input = test[0]
            expected = test[1]

            print("input=" + str(input) + " expected=" + str(expected))
            actual = s.minMeetingRooms(input)
            print("input=" + str(input) + " expected=" + str(expected) + " actual = " + str(actual))
            self.assertEqual(expected, actual)

