import unittest

from boggle.solution import Solution


class SortMergeTest(unittest.TestCase):

    DICTIONARY = ['yes', 'yet', 'day', 'red', 'yesterday', 'ray', 'steer', 'stead', 'drat', 'penguin']

    def test_sort_merge(self):
        s = Solution()

        bog_test = [['y', 'e', 's'],
                    ['r', 'e', 't'],
                    ['d', 'a', 'y']]

        expected = ['yes', 'yet', 'day', 'red', 'yesterday', 'ray', 'steer', 'stead', 'drat']
        expected.sort()

        output = s.boggler(bog_test, self.DICTIONARY)
        output = list(set(output)) # make list unique
        output.sort()
        print("output = ", output)
        print("expected = ", expected)

        self.assertEqual(expected, output)

    def test_partial_word_find(self):
        for w in self.DICTIONARY:
            val = w.find('ye', 0, len('ye'))
            if val == 0:
                print(w + " Begins with 'ye'")
