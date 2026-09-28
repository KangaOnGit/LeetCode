class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        queue = []

        longest_substring = 0
        for i in range(len(s)):

            if s[i] not in queue:
                queue.append(s[i])
            else:
                # if in queue
                # take latest element

                    # queue = [a, b], if s[i] = b
                    # -> queue = [b], longest_substring 2

                    # queue = [d, v] if s[i] = d
                    # -> queue = [v, d]

                longest_substring = max(longest_substring, len(queue))
                while s[i] in queue:
                    queue.pop(0)
                queue.append(s[i])

        # return max() because it doesn't count end element yet
        return max(longest_substring, len(queue))
