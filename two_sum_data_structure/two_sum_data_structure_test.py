
import unittest

from two_sum_data_structure.two_sum import TwoSum


class TwoSumDSTest(unittest.TestCase):

    def test_two_sum(self):

        tests = [
            # (["TwoSum", "add", "add", "add", "find", "find"],
            #  [[], [1], [3], [5], [4], [7]],
            #  [None, None, None, None, True, False]),
            # (["TwoSum", "add", "add", "find"], [[], [0], [0], [0]], [None, None, None, True]),
            (["TwoSum","add","add","add","add","find","find","find","find"],
             [  [],     [0],  [-1], [-1], [0],  [-2],   [0],  [-1],  [1]],
             [  None,   None, None, None, None,  True,  True, True,  False])
        # got [null, null, null, null, null,       true,  true, false, false]
        ]

        for test in tests:
            commands  = test[0]
            arguments = test[1]
            responses   = test[2]

            # don't create it before the command is invoked
            t = None

            for i in range(len(commands)):

                response = None

                if commands[i] == 'TwoSum':
                    t = TwoSum()
                elif commands[i] == 'add':
                    arg = arguments[i][0]
                    response = t.add(arg)
                    print("Add  : arg = " + str(arg) + " expected = " + str(responses[i]) + " actual = " + str(response))
                    self.assertEqual(responses[i], response)
                elif commands[i] == 'find':
                    arg = arguments[i][0]
                    response = t.find(arg)
                    print("Find : arg = " + str(arg) + " expected = " + str(responses[i]) + " actual = " + str(response))
                    self.assertEqual(responses[i], response)

