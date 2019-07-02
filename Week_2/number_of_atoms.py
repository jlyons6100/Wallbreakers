# Number of atoms: Counts number of atoms from an equation string

import re
from collections import Counter
class Solution:
    # Splits elems into element + number of atoms
    def handle_elem(self, elem, mult, counter):
        if elem == "":
            return
        match = re.match(r"([A-Z]+)(\w*)(\d*)", elem, re.I)
        if match:
            items = match.groups()
            try: 
                counter[items[0]] += int(items[1])*mult
            except:
                counter[items[0]] += 1*mult
        else:
            paren_num = re.findall(r'(\(.*\))|(\d+)', elem)
            new_form = paren_num[0][0]
            new_form = new_form[1:len(new_form) - 1]
            new_mult = mult
            try:
                new_mult = mult* int(paren_num[1][1])
            except:
                pass
            self.recurs(new_form, new_mult, counter)
    def recurs(self, formula, mult, counter):
        stack = 0
        cur = ""
        end_of_paren = False
        for ind in range(len(formula)):
            char = formula[ind]
            if char == "(":
                if stack == 0 and cur != "":
                    self.handle_elem(cur, mult, counter)
                    cur = ""
                stack += 1
                cur += char
            elif char == ")":
                stack -= 1  
                cur += char
                end_of_paren = True
            elif stack != 0:
                cur += char
            elif stack == 0:
                if end_of_paren == True:
                    while(ind <= len(formula) - 1 and formula[ind].isnumeric()):
                        cur += formula[ind]
                        ind += 1
                    self.handle_elem(cur, mult, counter)
                    cur = ""
                    end_of_paren = False
                elif char.isupper():
                    if cur != "": 
                        self.handle_elem(cur, mult, counter)
                    cur = ""
                    cur += char
                elif char.islower():
                    cur += char
                elif char.isnumeric() and cur != "":
                    cur += char
        self.handle_elem(cur, mult, counter)

    def countOfAtoms(self, formula: str) -> str:
        counter = Counter()
        self.recurs(formula, 1, counter)
        key_list = sorted(counter.keys())
        return "".join([key+str(counter[key]) if counter[key] != 1 else key for key in key_list])
        
        
