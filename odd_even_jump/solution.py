

class Solution:

    def oddEvenJumps(self, A):
        N = len(A)
        # returns a list of the index you can jump to from any index in A
        # runs twice since where you jump to on an even jump is diff than an odd jump
        def make(sorted_index_locations: [int]):
            # 'None' means no jump is possible from this index in A
            jump_to_locations = [None] * N

            # The stack is used to track indexes that you
            stack = []

            # now walk the list in order
            # if index_location > stack[-1], it means index_location is past stack[-1]
            # since sorted_index_locations is sorted smallest to largest, all smaller numbers are behind it
            # so it's finding the next-lowest number that's further up the list -- this is where it will jump to.

            for index_location in sorted_index_locations:
                while stack and index_location > stack[-1]:
                    # all items on the stack are smaller and are behind it in A
                    # so they'll jump to the same place this index will jump to
                    jump_to_locations[stack.pop()] = index_location
                # if stack is empty or this index is higher than the last on on the stack,
                # push this onto the stack and go to the next index
                stack.append(index_location)

            # jump_to_locations contains the location you jump, or None if you can't jump from that index
            return jump_to_locations

        B = sorted(range(N), key=lambda i: A[i])
        odd_jump_to_locations = make(B)
        B.sort(key=lambda i: -A[i])
        even_jump_to_locations = make(B)

        # odd and even have 'good indexes' where they end up True after this.
        # initialize assuming only that the very last location (A[N-1]) will always be True.
        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if odd_jump_to_locations[i] is not None:
                odd[i] = even[odd_jump_to_locations[i]]
            if even_jump_to_locations[i] is not None:
                even[i] = odd[even_jump_to_locations[i]]

        return sum(odd)

    def oddEvenJumps_make_stack(self, A: []) -> int:

        length = len(A)

        def make(sorted_index_array) -> [int]:
            ret = [None]*length
            stack = []

            for i in sorted_index_array:
                while stack and i > stack[-1]:
                    ret[stack.pop()] = i
                stack.append(i)
            return ret

        # this creates a new array of indexes into A, sorted in ascending order
        # range(length) creates the indexes 0-length-1
        index_array = sorted(range(length), key=lambda i: A[i])
        oddnext = make(index_array)

        # sort array now in descending order
        index_array.sort(key = lambda i: -A[i])
        evennext = make(index_array)

        # now create an array of False values, with one True at the end (where we need to jump to)
        odd = even = [False]*length
        odd[length-1] = even[length-1] = True

        for i in range(length-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)










        return 0


    # works, but is not performant enough for long A.
    def oddEvenJumps_bactrack(self, A: []) -> int:

        good_indexes = []
        length = len(A)

        ODD = 1
        EVEN = 2

        def backtrack(start: int, init_index: int, odd_even: int):

            # 3 things - reject, accept, or keep going
            # accept if on last item
            if start == length-1:
                # print("found a good index : " + str(init_index) + " val = " + str(A[init_index]))
                good_indexes.append(init_index)
                return

            next_index = start
            current_val = A[start]

            # print("New: start = " +str(start) + " init_index = " + str(init_index) + " odd_even = " +str(odd_even) + " curr_val = " + str(current_val))

            if odd_even == ODD: # A[i] <= A[j]
                can_jump, odd_even = False, EVEN
                smallest, next_index = None, start

                for i in range(start+1, length):
                    if A[i] >= current_val:
                        if smallest == None or A[i] < smallest:
                            smallest, next_index = A[i], i
                            can_jump = True
                if not can_jump:
                    # can't make a jump
                    return
            elif odd_even == EVEN:
                can_jump, odd_even = False, ODD
                largest, next_index =  None, start
                for i in range(start+1, length):
                    if A[i] <= current_val:
                        if largest == None or A[i] > largest:
                            largest, next_index = A[i], i
                            can_jump = True
                if not can_jump:
                    # can't make a jump
                    return

            backtrack(next_index, init_index, odd_even)

        for i in range(length):
            # print("trying val " + str(A[i]) + " at index " + str(i) + " out of " + str(length))
            backtrack(i, i, ODD)

        return len(good_indexes)




