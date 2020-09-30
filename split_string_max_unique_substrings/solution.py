# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def split_string_max_unique_substrings(self, s: str) -> [str]:   # note, actual just returns word count

        char_list = list(s)

        unique_list = []
        for i, char in enumerate(s):

            unique_list.append(str(char))
            if len(unique_list) == len(set(unique_list)):
                continue
            else:

                word = ' '.join(unique_list)
                spaces = []
                last_space = 0
                for i in range(word.count(' ')):
                    space_index = word.index(' ', last_space + 1)
                    spaces.append(space_index)
                    last_space = space_index

                for space in reversed(spaces):
                    chars = list(word)
                    chars[space + 1], chars[space] = chars[space], chars[space + 1]  # swap

                    new_word = ''.join(chars)
                    new_words = new_word.split()
                    if len(new_words) == len(set(new_words)):
                        unique_list = new_words
                        break
                    else:
                        chars = list(new_word)
                        if space == spaces[0]:
                            for j in range(len(new_word)-1,-1,-1):
                                if chars[j] == ' ':
                                    new_word = new_word[:j] + new_word[j+1:]
                                    break
                        word = new_word
                        word.index(' ', 0,)

        return unique_list








    def split_string_max_unique_substrings_recursive(self, s: str) -> [str]:   # note, actual just returns word count

        # 1. are we at bottom
        # 2. divide
        # 3. combine

        unique = False
        words = s.split()
        num_uniques = len(words)

        # change if words really are are unique
        if len(words) == len(set(words)):
            unique = True

        num_spaces = s.count(' ')
        num_ltrs = len(s) - num_spaces
        if num_spaces == num_ltrs - num_spaces - 1:  # 'abcdefghijklmnop' => 'a b c d e f g h i j k l m n o p'
            if unique:
                return num_uniques
            else:
                return -1

    def split_string_max_unique_substrings_r1(self, s: str, expected_result) -> [str]:  # note, actual just returns word count

        if len(s) == 1:
            return 1

        ltrs = set(list(s))

        counts = {}
        for ltr in ltrs:
            counts[ltr] = s.count(ltr)

        unique_count = 0
        for ltr, count in counts.items():
            if count == 1:
                index = s.index(ltr)
                if index == 0 or index == len(s)-1:
                    s = s.replace(ltr,'')
                    unique_count = unique_count + 1
                else:
                    prev = s[index-1]
                    next = s[index+1]
                    if counts[prev] == 1 and counts[next] == 1:
                        s = s.replace(ltr, '')
                        unique_count = unique_count + 1

        if len(s) == 0:
            return unique_count
        else:
            return unique_count + self.find_max(len(s)-1, s, expected_result - unique_count)

    def find_max(self, i, s, expected_result):
        from sortedcontainers import SortedSet

        unique, unique_count = False, -1
        words = s.split()
        if len(words) == len(set(words)):
            if len(words) == expected_result:
                print(words)
            unique_count = len(words)

        if i == 0:
            return unique_count

        a = self.find_max(i-1, s[:i] + ' ' + s[i:], expected_result)
        b = self.find_max(i-1, s, expected_result)

        return max(a,b,unique_count)


    book = set()

    def maxUniqueSplit(self, s: str) -> int:
        result = 0
        for i in range(1, len(s) + 1):
            curr = s[:i]
            if curr not in self.book:
                self.book.add(curr)
                result = max(result, 1 + self.maxUniqueSplit(s[i:]))
                self.book.remove(curr)
        return result












