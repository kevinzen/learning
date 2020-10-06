
from sortedcontainers import SortedList


class RecentCounter:

    def __init__(self):
        self.ping_set = SortedList()

    def ping(self, t: int) -> int:
        self.ping_set.add(t)
        ping_result = self.ping_set.irange(t - 3000, t, (True, True))
        return len(list(ping_result))


from collections import deque


class RecentCounterDeque:

    def __init__(self):
        self.slide_window = deque()
        self.slide_window.insert()

    def ping(self, t: int) -> int:
        # step 1). append the current call
        self.slide_window.append(t)

        # step 2). invalidate the outdated pings
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()

        return len(self.slide_window)

