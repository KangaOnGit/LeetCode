from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.user_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Timestamps for set is strictly increasing
            -> Sorted already
        """
        if key in self.user_dict:
            self.user_dict[key].append((timestamp, value))
        else:
            self.user_dict[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        """
        Get the Name and Timestamp then return the appropriate Value
        O(logn) time in total
            -> We can do dict lookup for names/key and Binary Search for Timestamp
                (O (1 + log(num_timestamps)))

        Cases:
            If cannot find timestamp but user exist
                Return value of the timestamp below it
            I.e: If there are timestamps [10, 20, 30]
            And user request timestamp 15
                -> return value at timestamp 10
            If user request timestmap 5
                -> return "" since theres no lower timestamp
        """
        if key not in self.user_dict:
            return ""
        timeValueList = self.user_dict[key]

        l = 0
        r = len(timeValueList) - 1
        res = ""
        while l <= r:
            mid = (l + r)//2
            time, value = timeValueList[mid]
            if time == timestamp:
                return value
            elif time < timestamp:
                """
                If the timestamp doesn't exist
                    and we want to get the value below it if theres any
                Since we only move left if we found a new lower-end bound
                    We can confidently save the last lower-end bound
                    Then we choose the most recent lower-end bound to return
                """
                res = value
                l = mid + 1
            else:
                r = mid - 1
        return res