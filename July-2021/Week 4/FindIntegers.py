# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones
class Solution:
    def findIntegers(self, n: int) -> int:
        one_less, zero_less, one_even, zero_even = 0, 0, 0, 1

        for b in bin(n)[2:]:

            # Find next value for each state
            new_one_less = zero_less
            new_zero_less = one_less + zero_less + \
                (zero_even + one_even) * (b == "1")
            new_one_even = zero_even * (b == "1")
            new_zero_even = (zero_even + one_even) * (b != "1")

            # Update all states
            one_less = new_one_less
            zero_less = new_zero_less
            one_even = new_one_even
            zero_even = new_zero_even

        return one_less + zero_less + one_even + zero_even


print(Solution().findIntegers(5))
