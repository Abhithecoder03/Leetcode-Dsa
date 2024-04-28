class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        div = [0] * n
        prefix_remainder = 0

        for i in range(n):
            prefix_remainder = (prefix_remainder * 10 + int(word[i])) % m
            if prefix_remainder == 0:
                div[i] = 1

        return div