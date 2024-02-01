class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0) # 1
        dividend, divisor = abs(dividend), abs(divisor) # 2
        res = 0 # 3
        while dividend >= divisor: # 4
                curr_divisor, num_divisors = divisor, 1 # 5
                while dividend >= curr_divisor: # 6
                    dividend -= curr_divisor # 7
                    res += num_divisors # 8
                    
                    curr_divisor = curr_divisor << 1 # 9
                    num_divisors = num_divisors << 1 # 10
                    
        if not positive: # 11
            res = -res # 12
            
        return min(max(-2147483648, res), 2147483647) # 13