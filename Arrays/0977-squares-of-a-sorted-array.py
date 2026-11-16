class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sql_list=[num**2 for num in nums]
        sql_list.sort()
        return sql_list 
