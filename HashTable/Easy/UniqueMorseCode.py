from typing import List


class Solution:
    def __init__(self):
        self.morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                          ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                          "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(["".join([self.morseCode[ord(ch)-97] for ch in word]) for word in words]))


print(Solution().uniqueMorseRepresentations("abc"))
