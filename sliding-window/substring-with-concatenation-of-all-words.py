from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        m = len(words) 
        n = len(s)

        Cleaner way rather than Iterative Sliding Window
            Take a Window of len(word_len * len(words))
        Check if every word in that window is in words
                    and add to queue
        Check that queue if is a permutation:
            .remove() -> O(m)
            "for word in..." -> O(m)
         => Time Complexity: O(n x m^2)

        Use hash table lookup with Counter -> O(n x m)
        To remove the need to initialize every Hashmap for each Sequence
            We use Offset -> O(n)
        """

        def worst_time_complex():
            """
                O( n x m^2)
                No Hashmap, just pure agony
            """
            word_len = len(words[0])
            out = []
            left, right = 0, word_len*len(words)
            while right <= len(s):
                seq = s[left : right]
                if self.check_seq(seq, words, s):
                    out.append(left)
                right += 1
                left += 1
            return out
        #eturn worst_time_complex()

        def med_time_complexity():
            """
                O(n x m) from building the hash
            """
            word_len = len(words[0])
            out = []
            # Create dict of value = frequency of each key/word in words
            target = Counter(words)

            left, right = 0, word_len*len(words)
            while right <= len(s):
                seq = s[left : right]
                if self.check_seq_hashmap(seq, target, word_len):
                    out.append(left)
                right += 1
                left += 1
            return out
        #return med_time_complexity()

        self.num_words = len(words)
        self.word_len = len(words[0])
        self.target = Counter(words)
        def optimal_approach():
            """
            No Hash -> From O(n x m) to O(n)
                in which m is length of words
            O(n) approach:
            Instead of rebuilding a frequency map
                for every candidate substring:
                    [bar foo]
                    [foo the]
                    [the bar]
            Maintain a running frequency map.

            When window moves:
                remove left word
                add right word

            Each word enters and leaves
                the window at most once.
            => O(n)
            """
            if not s or not words:
                return []

            out = []

            for offset in range(self.word_len):
                out.extend(self.scan_offset(s, offset))
            return out
        return optimal_approach()

    def check_seq(self, seq, words, s):
        queue = []
        word_len = len(words[0])
        i = 0
        while i < len(seq):
            word = seq[ (i) : (i + word_len) ]
            if word not in words:
                return False
            else:
                queue.append(word)
            if len(queue) == len(words):
                # O(m) lookup
                if self.check_queue(queue, words):
                    return True
            i += word_len
        return False

    def check_seq_hashmap(self, seq, target, word_len):
        freq = Counter()
        i = 0
        # O(m) Loop to Rebuild Counter
        while i < len(seq):
            word = seq[i:i + word_len]
            freq[word] += 1

            # early exit
                # O(1) lookup
            if freq[word] > target[word]:
                return False
            i += word_len
        return freq == target # Same dict

    def check_queue(self, queue, words):
        dummy = words.copy()
        for word in queue:
            if word in dummy:
                # O(m) remove
                dummy.remove(word)
        return len(dummy) == 0

    def scan_offset(self, s, offset):
        left = offset
        freq = defaultdict(int)
        words_in_window = 0

        out = []
        for right in range(
            offset, len(s) - self.word_len + 1,
            self.word_len):
            word = s[ right : (right + self.word_len) ]

            if word not in self.target:
                freq.clear()
                words_in_window = 0
                left = right + self.word_len
                continue
            freq[word] += 1
            words_in_window += 1

            # Exceed Window Length
            while freq[word] > self.target[word]:
                self.remove_left_word(s, freq, left)
                words_in_window -= 1
                left += self.word_len

            # Valid Window
            if words_in_window == self.num_words:
                out.append(left)
                self.remove_left_word(s, freq, left)
                words_in_window -= 1
                left += self.word_len
        return out
    
    def remove_left_word(self, s, freq, left):
        left_word = s[left : (left + self.word_len) ]
        freq[left_word] -= 1

"""
Cases:
- A chunk may not exist in words
- Duplicate words can exist
    ["aa", "aa"]
- Matches can overlap
    s = "aaaaaaaaaaaaaa"
    words = ["aa", "aa"]

Approach:
    Slide by character

Optimal approach:
    Process word-aligned windows
    for each possible offset
"""
