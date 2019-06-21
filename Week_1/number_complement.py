# Number Complement:
# Given a positive integer, outputs its complement number

class Solution:
    # flip_bits(bits): Flips bits in a list representing an integer value
    def flip_bits(self, bits: list) -> str:
        for ind in range(len(bits)):
            bits[ind] = "0" if bits[ind] == "1" else "1"
        return "".join(bits)
    # findComplement(num): Returns  the component of an input number
    def findComplement(self, num: int) -> int:
        bits = "{0:b}".format(num)
        bits = self.flip_bits(list(bits))
        return int(bits, 2)