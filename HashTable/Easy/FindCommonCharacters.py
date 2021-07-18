from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(*words)
        output = []
        for i in words[0]:
            temp = 0
            for j, k in enumerate(words[1:]):
                if i in k:
                    words[j+1] = k.replace(i, "", 1)
                    temp += 1
            if temp == len(words)-1:
                output.append(i)
        return output

    def commonCharsWords(self, words: List[str]) -> List[str]:
        occurences = {}
        for char in words[0]:
            occurences[char] = occurences.get(char, 0) + 1

        # check if chars exist in other words, if so, compute the lowest count/freq
        for char in occurences.keys():
            for i in range(1, len(words)):
                if char in words[i]:
                    occurences[char] = min(
                        occurences[char], words[i].count(char))
                else:
                    occurences[char] = 0
                    break

        # build the final result
        out = []
        for char, occurence in occurences.items():
            for i in range(occurence):
                out.append(char)

        return out


obj = Solution()
res = obj.commonChars(["bella", "label", "roller"])
print(res)
