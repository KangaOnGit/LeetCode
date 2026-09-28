from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Loop through strs
                Stop and Check Anagram

        2. Sort each word and put into a dict
            sorted_word = sort(word)
            dict[sorted_word].append(word)

        3. Count each char in a word
        
        -> 2 and 3 works because anagram are the same words.
            -> We take the similar elements of each word
            -> There number of characters and the word when sorted
        [ate, eat] -> both have same chars and number of chars
                   -> Both have the same sorted variation
        """
        if len(strs) <= 1:
            return [strs]
        
        def loop_and_check():
            """
                Time Limit Exceeded
            2 Loops -> O(n^2)
            self.check_anagram another 2 loops -> O(L^2)
                L = word1/word2 length
            => O(n^2 * L^2)
            """
            out = []
            visited = set()
            for idx1 in range(len(strs)):
                word1 = strs[idx1]
                if word1 in visited:
                    continue
                visited.add(word1)
                lst = [word1]
                for idx2 in range(idx1 + 1, len(strs)):
                    word2 = strs[idx2]
                    # O(1) Lookup
                    char = set(word1)
                    if self.check_anagram(char, word1, word2):
                        lst.append(word2)
                        visited.add(word2)
                out.append(lst)
            return out
        #return loop_and_check()

        def sorted_word():
            # Dictionary with Empty List Init
            word_dict = defaultdict(list)
            for word in strs:
                key = tuple(sorted(word))
                word_dict[key].append(word)
            return list(word_dict.values())
        #return set_check()
    
        def character_frequency():
            char_freq = defaultdict(list)
            for word in strs:
                count = defaultdict(int)
                for ch in word:
                    count[ch] += 1
                char_freq[tuple(sorted(count.items()))].append(word)
            return list(char_freq.values())
        #return character_frequency()

        def character_frequency2():
            char_freq = defaultdict(list)
            for word in strs:
                # Alphabetical Characters
                count = [0]*26
                for ch in word:
                    idx_char_in_alphabet = ord(ch)
                    count[idx_char_in_alphabet - ord("a")] += 1
                char_freq[tuple(count)].append(word)
            return list(char_freq.values())  
        return character_frequency2()    

    def check_anagram(self, char, word1, word2):
        if len(word1) != len(word2):
            return False
        for ch in char:
            # Can also use Counter()
            if word1.count(ch) != word2.count(ch):
                return False
        return True
        