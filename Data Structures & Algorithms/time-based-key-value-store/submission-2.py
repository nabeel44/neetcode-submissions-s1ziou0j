class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.mp[key]
        l, r = 0, len(lst) - 1
        while l <= r:
            m = (l + r) // 2
            if lst[m][0] < timestamp:
                l = m + 1
            elif lst[m][0] > timestamp:
                r = m - 1
            else:
                return lst[m][1]
        for i in range(len(lst) -1, -1, -1):
            if lst[i][0] <= timestamp:
                return lst[i][1]
        return ""


        
