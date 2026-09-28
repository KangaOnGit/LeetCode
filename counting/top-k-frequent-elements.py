import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def no_heap_no_counter(k):
            """
                Create Counter for nums
                    Create a lst and
                        only save the top K Frequency
            """
            # Key: num | Value: Freq
            num_dict = {}
            for idx in range(len(nums)):
                if nums[idx] in num_dict:
                    num_dict[nums[idx]] += 1
                else:
                    num_dict[nums[idx]] = 1

            lst = []
            for key, value in num_dict.items():
                if len(lst) == k:
                    # Find min frequency
                    min_vk = min(lst)
                    if value > min_vk[0]:
                        # Remove min freq and add curr freq
                        lst.remove(min_vk)
                        lst.append((value, key))
                else:
                    lst.append((value, key))
            return [item[1] for item in lst]
        #return no_heap_no_counter()

        def heap_counter():
            """
                Heap and Counter
            """
            count = Counter(nums)
            heap = []

            for key, value in count.items():
                # heappush is a min_heap operation
                    # -> Append negative value/frequency
                heapq.heappush(heap, (-value, key))

            res = []
            for i in range(k):
                # Pop Smallest Negative -> Largest Positive
                freq = heapq.heappop(heap)[1]
                res.append(freq)
            return res
        #return heap_counter()

        def bucket():
            """
            A Frequency can have many numbers
                -> A dictionary contains
                    dict[freq] = list[num with same frequency]
                -> ~ Buckets
            Lists as Buckets is faster than dict since
                                you need to revisit frequencies
            """

            count = Counter(nums)
            # Create N + 1 Frequency Buckets
            buckets = [[] for _ in range(( len(nums) + 1 ))]
            for num, freq in count.items():
                # Put number in respective frequency buckets
                buckets[freq].append(num)
            print(buckets)
            res = []
            # Loop backwards
                # Because we Create Frequency Buckets from
                    # Smallest to Largest Frequency
            freq = len(nums)
            while freq >= 0:
                bucket = buckets[freq]
                for num in bucket:
                    res.append(num)
                    if len(res) == k:
                        return res
                freq -= 1
        return bucket()
"""
Intuition for Buckets:
    Similar to Group Anagrams:
        Find a common property and group elements by that property.
            Anagrams -> character frequency
            Top K Frequent -> occurrence frequency
        You can use anagram approach of dictionary
            then use heap for easier sorting
            but bucket is more optimal if you want a SORTED RESULT

    Hashing (Counter) tells us:
        num -> frequency

    Buckets reverse the mapping:
        frequency -> [nums with that frequency]

    Since frequencies are bounded:
        1 <= frequency <= n

    We can use the frequency itself as an index.

    This gives us an implicitly sorted structure:
        bucket[1], bucket[2], ..., bucket[n]

    Traversing from n down to 1 visits elements
    from highest frequency to lowest without needing
    a heap or sorting.

    Therefore:
        Counter + Heap       : O(n + m log m)
        Counter + Sort       : O(n + m log m)
        Counter + Buckets    : O(n)

    where m = number of unique elements.
"""
