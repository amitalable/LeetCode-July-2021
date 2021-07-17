from collections import Counter, defaultdict


class Solution:
    def __init__(self) -> None:
        self.l = [sum(map(int, str(x))) for x in range(10**5+1)]

    def countBallsUsingCounter(self, lowLimit: int, highLimit: int) -> int:
        return max(Counter(self.l[lowLimit:highLimit+1]).values())

    def numberDigitSum(self, number: int) -> int:
        digitSum = 0
        while number > 0:
            digitSum += number % 10
            number //= 10
        return digitSum

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashTable = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            hashTable[self.numberDigitSum(i)] += 1
        return max(hashTable.values())


print(Solution().countBalls(11, 104))
print(Solution().countBallsUsingCounter(98, 999))
