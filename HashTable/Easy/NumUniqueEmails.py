# https://leetcode.com/problems/unique-email-addresses/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            email = email.split('@')
            if '+' in email[0]:
                email[0] = email[0][:email[0].index('+')]
            email[0] = email[0].replace(".", "")
            email = "@".join(email)
            uniqueEmails.add(email)
        return len(uniqueEmails)
