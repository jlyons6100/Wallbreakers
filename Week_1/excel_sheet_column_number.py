# Excel Sheet Column Number:
# Return column number  of excel sheet

class Solution:
    def titleToNumber(self, s: str) -> int:
        offset = ord("A") - 1 # 1-26 for A-Z
        total = 0
        mult = 1
        for ind in range(len(s)-1, -1, -1):
            ltr = s[ind]
            total +=  (mult*(ord(ltr) - offset))
            mult*= 26
        return total