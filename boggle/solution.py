class Solution(object):

    def boggler(self, grid, dictionary):

    # grid = the boggle board. [[]] grid is m rows by n cols
    # dictionary = allowable words

        m, n = len(grid[0]), len(grid)

        words = []
        # now walk the grid, left to right, top to bottom.
        # Top right corner = (0,0)
        for i in range(m):
                for j in range(n):
                    starting_point = (i,j)
                    coords_used = [starting_point]
                    starting_letter = str(grid[i][j])
                    print("starting letter = ", starting_letter)
                    words = words  + self.find_words(starting_letter, grid, starting_point, coords_used, dictionary)

        return words

    # frag = word frag to this point, including this letter
    # grid = the boggle board. [[]] grid is m rows by n cols
    # coords = x,y current location on grid
    # coords_used array of coords used already
    # dictionary = allowable words
    def find_words(self, fragment, grid, coords, coords_used, dictionary):
        # m = # cols, n = # rows
        m, n = len(grid[0]), len(grid)
        # x, y are where the current location we're looking at
        x, y = coords[0], coords[1]

        # 1. return if at the bottom
        #  -- in this case, return when adding letters does not result in a partial or whole word
        # 2. Divide
        #  -- for each letter, follow each path where there is a partial match.
        #  -- if we find a word, then capture it and keep going unless time to return
        # 3. Conquer
        #  -- add all words to a result

        # determine if we should return
        #  -- if current fragment cannot make a word

        word = self.is_whole_word(fragment, dictionary) # returns [] if no word, or ['word', 'other', 'words'], etc.
        if word:
            print("FOUND WORD! " + word[0])

        # m = row,  n = col
        # valid offsets for 0,0: (0,1), (1,0), (1,1)
        # invalid: (-1, -1), (-1, 0), (-1, 1), (0, -1), (1,-1)

        # valid offsets for 2,2: (-1,-1), (-1,0), (0,-1)
        # invalid: (-1, 1), (0, 1), (1, -1), (1, 0), (1,1)

        offsets = [(-1,-1), (-1, 0),  (-1, 1),  (0, -1),  (0, 1),  (1, -1),  (1, 0),  (1, 1)]
        sub_words = []
        for offset in offsets:
            new_x, new_y = x + offset[0], y + offset[1]
            new_coords = (new_x, new_y)
            if not (new_x < 0 or new_y < 0 or new_x >= m or new_y >= m):
                # print(new_coords, coords_used)
                if new_coords in coords_used:
                    continue
                new_letter = grid[new_x][new_y]
                new_fragment = fragment + new_letter
                if self.is_partial_word(new_fragment, dictionary):
                    coords_used += [(new_x, new_y)]
                    # print("new_coords", new_coords)
                    # print("new_fragment", new_fragment)
                    found_words = self.find_words(new_fragment, grid, new_coords, coords_used, dictionary)
                    if found_words:
                        sub_words = sub_words + found_words
                    print(sub_words)
                    coords_used.remove((new_x, new_y))

        # Merge Step
        return word + sub_words

    def is_whole_word(self, word, dict):
        if word in dict:
            return [word]
        else:
            return []

    def is_partial_word(self, word, dict):
        for each_word in dict:
            # print(each_word)
            if each_word[0:len(word)] == word:
                # print("word = ", word, " matches ", each_word[0:len(word)])
                # print("Partial word found ", word, len(word))
                return True
        # print("NOT Partial word ", word)
        return False
