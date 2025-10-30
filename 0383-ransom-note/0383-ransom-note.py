from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for ch in ransom_count:
            if ransom_count[ch] > magazine_count[ch]:
                return False
        return True
