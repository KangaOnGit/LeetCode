import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Constraints:
            h >= len(piles)
        -> k = 1 if h >>>>> len(piles)
            else:
                k in [min(piles), max(piles)]

        The best way to combat outliers like h >>> len(piles)
            is to do binary search
            where you take mid = (1B + 1) // 2
            and evaluate whether that mid is overshooting or undershooting the h
            if time taken < h then you we sure k in [bottom, mid - 1]
                elif time taken == h -> smallest_k = mid
                else: k in [mid + 1, upper]
        -> reduce the search space of [1, 1B]

        Reasoning:
            To combat h >>> len(piles) making k = 1
            We can try finding first if k is in [1, min(piles)]

            if min(piles) return time taken <= h -> We evaluate [1, mid - 1]
            if time taken > h then k MUST be in range [min(piles), max(piles)]
                k cannot be outside of max(piles) (Intuition, hard to explain)
        """
        def intuition():
            smallest_pile = min(piles)  # O(n)
            smallest_k = 10**9

            time_taken = 0
            for i in range(len(piles)):
                time_taken += math.ceil(piles[i] / smallest_pile)

            if time_taken == h:
                return smallest_pile

            elif time_taken < h:
                lower = 1
                upper = smallest_pile
                smallest_k = smallest_pile

                while lower <= upper:
                    tt = 0
                    mid = (lower + upper) // 2

                    for i in range(len(piles)):
                        tt += math.ceil(piles[i] / mid)

                    if tt == h:
                        # mid works, but there may be a smaller k
                        smallest_k = mid
                        upper = mid - 1

                    elif tt < h:
                        # mid works, so search for something smaller
                        smallest_k = min(smallest_k, mid)
                        upper = mid - 1

                    else:  # tt > h
                        # mid is too slow
                        lower = mid + 1

                return smallest_k

            elif time_taken > h:
                lower = smallest_pile + 1
                upper = max(piles)

                while lower <= upper:
                    tt = 0
                    mid = (lower + upper) // 2

                    for i in range(len(piles)):
                        tt += math.ceil(piles[i] / mid)

                    if tt <= h:
                        # mid works; try smaller
                        smallest_k = min(smallest_k, mid)
                        upper = mid - 1

                    else:  # tt > h
                        # mid is too slow
                        lower = mid + 1

                return smallest_k
        #return intuition()

        def more_polished():
            """
            Since we found the upper-bound to be max(piles)
            -> k must be in [1, max(piles)]
            """

            lower = 1
            upper = max(piles)

            while lower <= upper:
                mid = (lower + upper) // 2

                time_taken = sum(
                    (pile + mid - 1) // mid
                    for pile in piles
                )

                if time_taken <= h:
                    upper = mid - 1
                else:
                    lower = mid + 1

            return lower
        return more_polished()