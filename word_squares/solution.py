
class Solution:


    def wordSquares(self, words):

        from itertools import permutations

        # babaabatbabaatan
        # 0123456789012345
        # b/0 == 0, a/1 = 4, b/2 == 8, a/3 = 12
        # a/4 = 1, b/5 == 5, a/6 == 9, t/7 == 13
        # b/8 = 2, a/9 = 6, b/10 = 10, a/11 == 14
        # b/12 = 3, a/13 = 7, b/14 = 11, a/15 == 15

        word_size = len(words[0])
        num_words = len(words)
        square_size = word_size * word_size
        solutions = []

        # get all options
        bigger_set = []
        for i in range(word_size):
            bigger_set.extend(words)
        all_options = permutations(iterable=bigger_set, r=word_size)
        all_options = list(set(all_options))

        for option in all_options:
            option = list(option)
            option_works = self.does_option_work(option, square_size, word_size)
            if option_works and option not in solutions:
                solutions.append(option)

        return solutions

    def does_option_work(self, option, square_size, word_size):
        big_string = list("".join(option))
        option_works = True
        for i in range(square_size):
            index = (i // word_size + (i % word_size) * word_size)
            if big_string[i] != big_string[index]:
                option_works = False
        return option_works

    def wordSquares1(self, words):

        from itertools import permutations

        word_size = len(words[0])
        num_words = len(words)
        square_size = word_size * word_size
        solutions = []

        # get all options
        bigger_set = []

        # 5467 => 7 = 5467 % 1000.
        # 7 = (5467 // 1) % 10,
        # 6 = (5467 // 10) % 10,
        # 4 = (5467 // 100) % 10
        # 5 = (5467 // 1000) % 10
        for i in range(num_words**(word_size-1)):
            option = []
            for j in range(word_size):
                offset = (i // num_words**j) % num_words
                option.append(words[offset])
            print(option)
            option_works = self.does_option_work(option, square_size, word_size)

            if option_works and option not in solutions:
                solutions.append(option)

        return solutions

