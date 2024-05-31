class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        overall_xor = 0
        for n in nums:
            overall_xor ^= n
        first_group_xor = 0
        second_group_xor = 0

        bit_pos_dif = 0
        while (overall_xor >> bit_pos_dif) & 1 != 1:
            bit_pos_dif += 1

        for num in nums:
            if (num >> bit_pos_dif) & 1 == 1:
                first_group_xor ^= num
            else:
                second_group_xor ^= num

        return [first_group_xor, second_group_xor]