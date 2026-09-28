from collections import Counter, defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        AAABBBB | k = 1 => AABBBBB => 5

        ABCDCCD | k = 2 -> AB-CCCCC => 5
        0123456 | 3 and 6 idx
        """

        def own_solution():
            """
            Doesn't working because it's directional
            Doesn't consider Left but only Right-forward
            """
            l, r = 0, 1
            max_len = 0
            while r <= len(s):
                sequence = s[l:r]
                majority_char = Counter(sequence).most_common(1)[0][0]

                cnt, expand = k, 1
                while cnt >= 0:
                    char = s[r + expand - 1:r + expand]
                    if char != majority_char:
                        cnt -= 1
                    if cnt < 0:
                        break
                    sequence += char
                    expand += 1
                l += 1
                r += 1
                max_len = max(max_len, len(sequence))
            return max_len

        def sol(s):
            """
            Sequence: A A B A C
            To make the maxed window size, we need to replace B and C
            A: 3
            B: 1
            C: 1
            -> Pick based on the highest-frequency
            This is only possible if: sequence_len - highest_freq <= k
                                    (If it's > k then it's not possible)
            Rudimentary Observation.
            
            But, when will you move the left side for another window?
                We move the Left Side if sequence_len - highest_freq > k
                    Because we know that window isn't possible if it's larger than k.
            Sequence := Window (Used interchangably)
            """
            count = defaultdict(int)

            l = 0
            highest_freq = 0
            ans = 0

            for r in range(len(s)):
                right_most_char = s[r]
                count[right_most_char] += 1

                # Highest frequency character in the current window
                highest_freq = max(highest_freq, count[right_most_char])
                seq_len = r - l + 1

                # Too many characters need replacing
                while seq_len - highest_freq > k:
                    left_most_char = s[l]
                    count[left_most_char] -= 1
                    l += 1

                    seq_len = r - l + 1

                ans = max(ans, r - l + 1)
            return ans
        return sol(s)