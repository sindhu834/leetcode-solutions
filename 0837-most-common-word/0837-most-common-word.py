import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # 1. Normalize paragraph: lowercase & remove punctuation
        words = re.findall(r'\w+', paragraph.lower())  # extracts words only
        
        # 2. Create a set for banned words for O(1) lookups
        banned_set = set(banned)
        
        # 3. Count frequencies of non-banned words
        word_count = Counter(word for word in words if word not in banned_set)
        
        # 4. Return the most common word
        return word_count.most_common(1)[0][0]
