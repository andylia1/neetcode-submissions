class TimeMap:

    def __init__(self):
        # dict of key: string, value: [[string, timestamp]]
        self.hmp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.hmp:
            l, r = 0, len(self.hmp[key]) - 1
            while l <= r:
                m = (l + r) // 2
                if self.hmp[key][m][1] > timestamp:
                    r = m - 1
                else:
                    res = self.hmp[key][m][0]
                    l = m + 1
        
        return res
        
