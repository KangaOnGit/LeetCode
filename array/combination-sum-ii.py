class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []
        def backtrack(
            rem: int,
            idx: int,
            lst: list,):
            """
            Cases:
                - Skip current number
                - Take current number

            We cannot take the same number (at the same index) multiple times
                [1, 2, 1]
                    -> Cannot take 1 at the 0th Index multiple times,
                        but can take at 2nd index.
            
                Since there are duplicate numbers, we can use memoization/caching
                    (Since duplicate numbers mean we have seen this result before)
                    Problem with this memoization is said below.
                        It's only different if the index itself is different

                [2, 2 , 1]
                Theres no point in computing the 2 at idx 1 because since its right next to 
                    the 2 at idx 0, it will have the same combination regardless
                    It's only different when the index is not adjacent:
                            [2, 3, 2, 1]
                    Since the index is not adjacent, the 2 at index 2 cannot see the 3 at idx 1
                        -> different combination
            """

            if rem == 0:
                if sorted(lst) not in res:
                    res.append(sorted(lst))
                return
            elif idx == len(candidates) or rem < 0:
                return

            # Take current number
            lst.append(candidates[idx])
            backtrack(rem - candidates[idx], idx + 1, lst)

            # Skip current number (or remove it from list, same thing)
            lst.pop()

            # Skip adjacent duplicate
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx = idx + 1
            backtrack(rem, idx + 1, lst)

        #backtrack(target, 0, [])
        #return res

        candidates.sort()
        def backtrack_with_loop(rem, idx, lst):
            """
            Basically the above but faster because:
                - Skip dupes
                - Sort list so can also skip numbers > rem
            """
            if rem == 0:
                if sorted(lst) not in res:
                    res.append(sorted(lst))
                return
            
            if idx == len(candidates) or rem < 0:
                return

            for i in range(idx, len(candidates)):

                # Skip dupes value
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                # since candidate is sorted, every i + 1 is larger than i
                if candidates[i] > rem:
                    break

                # take curr num
                lst.append(candidates[i])
                backtrack_with_loop(rem - candidates[i], i + 1, lst)

                # take next num skip curr num
                lst.pop()

        backtrack_with_loop(target, 0, [])
        return res