class Solution(object):

    # target = word
    # combo = list of coordinates for letters to here
    # current_coord = x,y to current square

    # grid = m x n array => e.g., if grid = [ ['y', 'e', 's'], ['r', 'e', 't'], ['d', 'a', 'y'] ]
    # top left = (0,0).
    # grid[0][0] = 'y', grid[0][1] = 'e', grid[2][0] = 'd'

    # here, now try all squares next to the word that we haven't already used...

    # 0,0 => 0,1 / 1,1 / 1,0
    # 2,2 =>  1,1 / 1,2 / 2, 1
    # 1,1 => 0,0 / 1, 0 / 2,0 / 1,0 / 1,2 / 2,0 / 2,1 / 2,2

    # from cur_j - 1, cur_j + 1 & cur_i - 1, cur_i + 1

    def boggler(self, grid, dictionary):

        offsets = [(-1,-1), (-1, 0),  (-1, 1),  (0, -1),  (0, 1),  (1, -1),  (1, 0),  (1, 1)]
        results = []
        m, n = len(grid), len(grid[0])
        grid_size = m * n

        def backtrack(cur_word, combo, cur_coords):

            cur_i = cur_coords[0]
            cur_j = cur_coords[1]

            if is_whole_word(cur_word):
                results.append(cur_word)
                # don't return bc we can have found a partrial word
            elif not is_partial_word(cur_word) or len(combo) == grid_size:
                return

            for offset in offsets:

                new_i, new_j = cur_i + offset[0], cur_j + offset[1]
                new_coord = (new_i, new_j)
                if is_valid_coord(new_coord) and new_coord not in combo:

                    combo.append(new_coord)
                    backtrack(cur_word + str(grid[new_i][new_j]), combo, new_coord)
                    combo.pop()

        def is_valid_coord(coord):
            valid_x = 0 <= coord[0] < m
            valid_y = 0 <= coord[1] < n
            return valid_x and valid_y

        def is_whole_word(word):
            if word in dictionary:
                return [word]
            else:
                return []

        def is_partial_word(word):
            for each_word in dictionary:
                # print(each_word)
                if each_word[0:len(word)] == word:
                    # print("word = ", word, " matches ", each_word[0:len(word)])
                    # print("Partial word found ", word, len(word))
                    return True
            # print("NOT Partial word ", word)
            return False

        for i in range(m):
            for j in range(n):
                backtrack(str(grid[i][j]), [(i,j)], (i,j))

        return results

