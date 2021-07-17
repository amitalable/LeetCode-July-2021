from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashTable = defaultdict(int)
        for each in cpdomains:
            each = each.split(" ")
            hashTable[each[1]] += int(each[0])
            part = each[1].split(".")
            if len(part) == 3:
                part[1] = part[1]+"."+part[2]
            for pt in part[1:]:
                hashTable[pt] += int(each[0])
        return [str(val) + " " + key for key, val in hashTable.items()]


domainList = ["900 google.mail.com", "50 yahoo.com",
              "1 intel.mail.com", "5 wiki.org"]

obj = Solution()
res = obj.subdomainVisits(domainList)
print(res)
