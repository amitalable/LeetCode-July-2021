# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = ""  # Used to store final result.
        i = 0
        while(i < len(dominoes)):
            # if charAt(i) is 'L' or 'R', just place append the same in res.
            if dominoes[i] == 'L' or dominoes[i] == 'R':
                res += dominoes[i]
                i += 1
            else:  # dominoes[i]=='.':
                # if charAt(i) is '.' and previous is Right pushed then, we have to count the
                # number of '.' (dots) and see what is at the other end of dot.
                if i > 0 and dominoes[i-1] == 'R':
                    j = i
                    while(j < len(dominoes) and dominoes[j] == '.'):
                        j += 1
                    countDots = (j-i)  # count of number of '.'(dots)
                    # if the other end is last index or if dominoe at other end is right pushed then
                    # there is nothing to cancel the right pushed force of first dominoes and so all
                    # '.'(dots) will be rightly pushed
                    if j == len(dominoes) or dominoes[j] == 'R':
                        res += 'R'*countDots
                    else:  # if other end is 'L' i.e, left pushed
                        # first half will be rightly pushed and second half is leftly pushed and
                        # if count is odd, then force on middle one gets cancelled
                        res += 'R'*(countDots//2) + '.'*(countDots -
                                                         2*(countDots//2)) + 'L'*(countDots//2)
                    i = j
                # if the start of string is '.'(dot) or previous is not rightly pushed
                else:
                    j = i
                    while(j < len(dominoes) and dominoes[j] == '.'):
                        j += 1
                    countDots = (j-i)  # count the number of dots

                    # if the other end is last index or if dominoe at other end is right pushed
                    # then there is no force at all on stating indexes. So, all will remains '.'
                    if j == len(dominoes) or dominoes[j] == 'R':
                        res += '.'*countDots
                    # if other end is left pushed, the all the starting will be pushed left
                    else:
                        res += 'L'*countDots
                    i = j

        return res
