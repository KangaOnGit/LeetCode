class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(rem: int, idx, lst):
            """
            For every number in candidates, we can either:
                - Move onto the next number
                - Stay at the current number
            """
            if rem == 0:
                if sorted(lst) not in res:
                    res.append(sorted(lst))
                return
            elif rem < 0 or idx == len(candidates):
                return

            lst.append(candidates[idx])

            # stay at current number
            backtrack(rem = rem - candidates[idx], idx = idx, lst = lst)

            lst.pop()

            # get next num instead
            backtrack(rem = rem, idx = idx + 1, lst = lst)

        #backtrack(rem = target, idx = 0, lst = [])
        #return res

    
        def backtrack_with_loop(rem: int, idx, lst):
            if rem == 0:
                if sorted(lst) not in res:
                    res.append(sorted(lst))
                return
            elif rem < 0 or idx == len(candidates):
                return

            for i in range(idx, len(candidates)):
                lst.append(candidates[i])

                backtrack_with_loop(rem - candidates[i], i, lst)
                lst.pop()

                # Don't need another backtrack_with_loop(rem, i + 1) call
                # Because after its popped, the loop will continue and it will automatically move i to i + 1
        backtrack_with_loop(target, 0, [])
        return res