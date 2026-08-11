class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        for sentence in sentences:
            word_count=len(sentence.split())
            if word_count>maximum:
                maximum=word_count
        return maximum

        