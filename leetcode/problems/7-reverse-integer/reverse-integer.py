class Solution:
    def reverse(self, x: int) -> int:

        if x.bit_length()>=32:
            return 0

        reverse = int(str(abs(x))[::-1])
        print(reverse)

        if (reverse.bit_length()>=32):
            return 0

        if x<0:
            return -reverse
        
        return reverse