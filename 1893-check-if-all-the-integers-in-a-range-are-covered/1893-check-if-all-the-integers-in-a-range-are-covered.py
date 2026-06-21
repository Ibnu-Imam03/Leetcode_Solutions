class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        covered = set() # 1 2 3 ....10 10 ..20

        for start, end in ranges:
            for num in range(start, end + 1):
                covered.add(num)

        for num in range(left, right + 1): # 21 ..21 
            if num not in covered:
                
                return False

        return True