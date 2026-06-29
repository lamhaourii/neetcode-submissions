class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenght= len(numbers)
        for i in range(lenght-1):
            left= i
            right= lenght-1
            while left<right:
                if numbers[left]+numbers[right]==target:
                    return [left+1, right+1]
                right-=1
        