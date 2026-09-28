from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Intuition:
            - The Minimum Window Substring must ALWAYS start
                with the character in t
                    => If we see a char in t
                        => Expand from that char
            
            - We create 2 dictionary for easier lookup time
                (Although the Space Complexity will be O(2T) where T is len(t))

            - If a character in dummy_dict, we deduct its count
                    if its count <= 0
                        => delete that key/char from dict
                        if dummy_dict is empty // len() == 0:
                            => We found the substring
        """

        def intuition():
            """
                Time: O(S^2)
                Space: O(T)
            """
            if len(s) < len(t):
                return ""

            target_dict = Counter(t) # O(T) where T is len(t)
            shortest_substring = ""

            # O(S) where S is len(S)
            for l in range(len(s) - len(t) + 1):
                left_char = s[l]

                if left_char in target_dict: # If find char begin window
                    dummy = t.replace(left_char, "", 1)
                    dummy_dict = Counter(dummy) # ~O(T)
                    
                    if len(dummy_dict) == 0:
                        # for cases where s = "ab" and t = "a"
                        substring = s[l]
                        if shortest_substring == "" or len(substring) < len(shortest_substring):
                            shortest_substring = substring

                    # ~O(S)
                    for r in range(l + 1, len(s)): # Expand window
                        right_char = s[r : r + 1]
                        if right_char in dummy_dict:
                            dummy_dict[right_char] -= 1 # Deduct count
                            if dummy_dict[right_char] <= 0:
                                del dummy_dict[right_char] # Delete char if count <= 0
                            if len(dummy_dict) == 0:
                                substring = s[l : r + 1]
                                if shortest_substring == "" or len(substring) < len(shortest_substring):
                                    shortest_substring = substring
            return shortest_substring
        #return intuition()

        def optimal_sol():
            """
                Time: O(S + T)
                Space: O(T)
            """
            if len(s) < len(t):
                return ""

            # Frequency of characters we still need
            need = Counter(t)

            # Number of characters still missing
            missing = len(t)

            left = 0

            # Store the best window as (length, left, right)
            best_len = float("inf")
            best_l = 0

            for right in range(len(s)):
                char = s[right]

                # If this character is still needed,
                # we've satisfied one required character.
                if need[char] > 0:
                    missing -= 1

                # Consume the character.
                need[char] -= 1

                # Window contains every character in t.
                while missing == 0:

                    # Update answer if this window is smaller.
                    window_len = right - left + 1
                    if window_len < best_len:
                        best_len = window_len
                        best_l = left

                    # Remove leftmost character.
                        # Rather than Restarting Window every Iteration
                        # We just contract the window while updating dictionary
                        # This remove the need to re-expand the window every time
                    left_char = s[left]
                    need[left_char] += 1

                    # If it becomes positive,
                    # we are now missing one required character.
                    if need[left_char] > 0:
                        missing += 1

                    left += 1

            if best_len == float("inf"):
                return ""

            return s[best_l:best_l + best_len]
        return optimal_sol()