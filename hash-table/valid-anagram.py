class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approaches:
            1. Create Dictionary for s and t then compare dicts
                O(n) Time and Space

            2. Loop through t, if found char in s:
                delete that char in s
                    else False

            3. Built-in count function
                string.count(char)
            
            4. Counter(word1) != Counter(word2)
                Same as 3 but more efficient
        """
        def check_del(s):
            for char in t:
                if char not in s:
                    return False
                s = s.replace(char, "", 1)
            return len(s) == 0
        #return check_del(s)

        def count_func():
            # Hashmap for O(1) Lookup
                # O(n) Space
            char = set(s)
            if len(s) != len(t):
                return False
            for ch in char:
                # Count number of Char in a String
                if s.count(ch) != t.count(ch):
                    return False
            return True
        #return count_func()
    
        def sort_check():
            return sorted(s) == sorted(t)
        return sort_check()