import unittest

from g_unique_emails.solution import Solution


class UniqueEmailsTest(unittest.TestCase):

    def test_solution(self):

        s = Solution()
        tests = [
            (["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"], 2),
        ]

        for test in tests:
            vals   = test[0]
            expected = test[1]

            print("vals = " + str(vals) + " expected_list = " + str(expected))

            actual = s.unique_emails(vals)

            print("vals = " + str(vals) + " expected = " + str(expected) + " actual = " + str(actual))

            # self.assertEqual(expected_list, actual)
