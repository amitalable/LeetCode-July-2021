# https://leetcode.com/problems/gray-code/

from typing import List


class Solution:
    def grayCodeUsingFormula(self, n: int) -> List[int]:
        # g(n) =  n xor n/2
        result = [i ^ (i // 2) for i in range(2**n)]
        return result

    def grayCodeUsingBruteForce(self, n: int) -> List[int]:
        l = [0, 1]
        for i in range(2, 2**n):
            x = bin(i)[2:]  # Convert into binary form
            y = x[1:]  # Take every bit except Most Significant Bit(MSB)
            z = x[:-1]  # Take every bit except Least Significant Bit(LSB)
            res = x[0]  # Take MSB
            for j in range(len(y)):
                # Change the each value to 0 if both y's bit and z's bit are same
                # Performing XOR
                if y[j] == z[j]:
                    res += "0"
                else:
                    res += "1"
            # Converting the binary into decimal and adding to the list
            l.append(int(res, 2))
        return l


if __name__ == "__main__":
    n = 4
    # 0,1,11,10,110,111,101,100,1100,1101,1111,1110,1010,1011,1001,1000
    print(Solution().grayCodeUsingFormula(n))
    print(Solution().grayCodeUsingBruteForce(n))
