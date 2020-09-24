import unittest


class SortedContainersTest(unittest.TestCase):

    def test_containers(self):
        from sortedcontainers.sortedlist import SortedList
        from sortedcontainers.sortedset import SortedSet

        a = [1,2,3,3,2,1,1,2,3,4,6,9,8,8,8,6,5,5,9,8,5,4]
        # SortedList =
        # [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6,6,8,8,8,8,9,9]
        # [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1]

        sl = SortedList(a)
        self.assertEqual(len(a), len(sl))

        # index to last spot before the first 4
        test_val = sl.bisect_left(4)
        self.assertEqual( 9, test_val)

        # index to the first spot after the last 4
        test_val = sl.bisect_right(4)
        self.assertEqual(11, test_val)

        # iterator for a range based on values
        test_val = list(sl.irange(4,6,(True, True)))
        self.assertEqual([4, 4, 5, 5, 5, 6, 6], test_val)

        # iterator for a range based on indexes
        test_val = list(sl.islice(2,12))
        self.assertEqual([1,2,2,2,3,3,3,4,4,5], test_val)

        # index to the first 4 in the list
        test_val = sl.index(4)
        self.assertEqual(9, test_val)

        # index to the last spot in the list
        test_val = sl.bisect_right(99)
        self.assertEqual(len(sl), test_val) # 22

        # index to the first spot in the list
        test_val = sl.bisect_right(-1)
        self.assertEqual( 0, test_val)

        # number of '4's in the list:
        test_val = sl.bisect_right(4) - sl.bisect_left(4)
        self.assertEqual(2, test_val)
        test_val = sl.count(4)
        self.assertEqual(2, test_val)

        # number of '0's in the list
        test_val = sl.bisect_right(0) - sl.bisect_left(0)
        self.assertEqual(0, test_val)
        test_val = sl.count(0)
        self.assertEqual(0, test_val)

        # SortedSet = [1,2,3,4,5,6,8,9]
        ss = SortedSet(a)

        # last index before the 4, if there
        test_val = ss.bisect_left(4)
        self.assertEqual(3, test_val)

        # first index before the 4, if there
        test_val = ss.bisect_right(4)
        self.assertEqual(4, test_val)

        # index to add new element at the end. = len(sl)
        test_val = ss.bisect_left(10)
        self.assertEqual(8, test_val)

        # index to add new element at the end. = len(sl)
        test_val = ss.bisect_right(10)
        self.assertEqual(8, test_val)

        # index to add the first element
        test_val = ss.bisect_left(0)
        self.assertEqual(0, test_val)

        # index to add the first element
        test_val = ss.bisect_right(0)
        self.assertEqual(0, test_val)


