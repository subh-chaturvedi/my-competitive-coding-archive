class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            mapped_num_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num_str)
        
        return sorted(nums, key=get_mapped_value)
