class TimeMap:

    def __init__(self):
        #map of key word, value [[timestamp, val]]
        self.hmp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        lst = self.hmp[key]
        l, r = 0, len(lst) - 1
        max_stamp = -1
        
        while l <= r:
            m = ( l + r) // 2

            if lst[m][0] > timestamp:
                r = m - 1
            else:
                max_stamp = max(max_stamp, m)
                l = m + 1
        
        if max_stamp != -1:
            return lst[max_stamp][1]
        else:
            return ""        
