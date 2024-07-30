class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        s = s.replace(" ", "")
        for char in s:
            if not self.isAlphaNumeric(char):
                print(char)
                s = s.replace(char, "")
        print(self.isAlphaNumeric(':'))
        return s == s[::-1]
    def isAlphaNumeric(self, s: str) -> bool:
        for char in s:
            if (65 <= ord(char)  <= 90) or (97 <= ord(char) <= 122) or (48 <= ord(char)  <= 57):
                return True
            else:
                return False