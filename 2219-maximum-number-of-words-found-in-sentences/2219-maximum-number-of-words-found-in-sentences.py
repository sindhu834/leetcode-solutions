class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words=0
        for s in sentences:
            word_count= len(s.split())#splits te sentences into words
            max_words=max(max_words,word_count)
        return max_words

        