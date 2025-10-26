class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Step 1: Create a set of unique words
        words_set = set(words)
        
        # Step 2: Remove all words that are suffixes of others
        for word in words:
            for i in range(1, len(word)):
                words_set.discard(word[i:])  # remove suffix
        
        # Step 3: Each remaining word contributes len(word) + 1 to encoding length
        return sum(len(word) + 1 for word in words_set)
