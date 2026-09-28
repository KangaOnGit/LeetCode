from collections import Counter, defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
            Approach:
                1. Heap (Sort by Frequency)
                2. Buckets
        Intuition:
            Group Similar Words/Sentences
        -> Frequency Dictionary ( dict[freq].append(word) )

            Top K Occurence/Frequency
        -> Frequency Dictionary
                1. Frequency Heap (push Negative Frequency and pop results)
                2. Frequency Buckets (N + 1 Frequency Buckets)

        ===> Find Similarity and group them BY THAT SIMILARITY.
        """

        def heap_counter():
            count = Counter(words)
            freq_dict = defaultdict(list)
            for word, freq in count.items():
                freq_dict[freq].append(word)
            
            heap = []
            for freq, word_lst in freq_dict.items():
                # Push Negative Frequency
                    # heappush is a min operator
                heapq.heappush(heap, (-freq, word_lst))

            res = []
            while heap:
                word_lst = heapq.heappop(heap)[1]
                # Sorted so it's in lexicographical order
                for word in sorted(word_lst):
                    res.append(word)
                    if len(res) == k:
                        return res
        #return heap_counter()

        def buckets():
            """
                Basically an Increasing Frequency List
                    Where idx = Frequency
            """
            buckets = [[] for _ in range(len(words) + 1)]
            count = Counter(words)
            for word, freq in count.items():
                buckets[freq].append(word)

            res = []
            freq = len(buckets) - 1
            while freq >= 0:
                bucket = buckets[freq]
                for word in sorted(bucket):
                    res.append(word)
                    if len(res) == k:
                        return res
                freq = freq - 1
        return buckets()
