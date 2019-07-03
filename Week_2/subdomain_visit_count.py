# Subdomain Visit Count: Returns subdomain visit counts

from collections import Counter
import re
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = Counter()
        for website in cpdomains:
            split = re.split(r'[ .]', website)
            num = split[0]
            string = ""
            for x in range(len(split) - 1, 0, -1):
                if string == "":
                    string += split[x]
                else:
                    string = split[x] + "."+string
                c[string] += int(num)
        return [str(c[key]) + " " + key for key in c]
        
