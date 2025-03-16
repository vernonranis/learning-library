from typing import List, Optional


class Solution:
    @staticmethod
    def method_1(nums: List[int], target: int) -> Optional[List[int]]:
        """
        This method is a brute force way of solving the problem

        Args:
            nums (List[int]): user input
            target (int): _description_

        Returns:
            Optional[List[int]]: _description_
        """        
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index1 != index2 and value1 + value2 == target:
                    return [index1, index2]


solution = Solution()
result = solution.method_1([2, 7, 11, 15], 9)
print(result)