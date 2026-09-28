from collections import Counter
class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Intuition:

            Loop through s2
                If char in s1 then:
                    Expand from char to seq_len (s2[idx:idx + seq_len])
                    if sort(s2[idx:idx + seq_len]) == sort(s1):
                            return True
            return False
        """

        def window():
            """
                O(n) where n is the length of s2
                O(m logm) where m is the length of s1 (double sorted)
            Time complexity: O(n * mlogm)

            A faster approach is to:
                When meet a character
                    Rather than expand right away
                        You expand iteratively and append it to a dictionary
                        Compare the 2 dictionary
                            If match -> return True else False
            """
            seq_len = len(s1)
            cnt = Counter(s1)

            for r in range(len(s2) - seq_len + 1):
                char = s2[r]
                if char in cnt:
                    seq = s2[r:r + seq_len]
                    if sorted(seq) == sorted(s1):
                        return True
            return False
        #return window()

        def window_but_dict():
            """
                O(n) where n is length of s2
                O(m) where m is the length of s1
            Time Complexity: O(n * m)
            
                O(m) where m is the length of s1
            Space Complexity: O(m)
            """
            seq_len = len(s1)
            cnt = Counter(s1)

            for r in range(len(s2) - seq_len + 1):
                char = s2[r]
                if char in cnt:
                    mock_dict = defaultdict(str)
                    mock_dict[char] = 1

                    # seq_len - 1 since char is already in cnt
                    for i in range(seq_len - 1):
                        next_char = s2[r + 1 + i: r + i + 2]
                        if next_char in cnt:
                            if next_char in mock_dict:
                                mock_dict[next_char] += 1
                            else:
                                mock_dict[next_char] = 1
                        else:
                            break

                    if mock_dict == cnt:
                        return True

            return False
        return window_but_dict()