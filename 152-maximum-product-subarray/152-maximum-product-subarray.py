class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def get_max(numbers):
            largest_prod = -math.inf
            current_prod = 1
        
            for num in numbers:
                current_prod *= num
                largest_prod = max(current_prod, largest_prod)
                
                # Reset if 0 is seen
                if current_prod == 0: current_prod = 1
            
            return largest_prod
        
        
        return max(
            get_max(nums), 
            get_max(reversed(nums))
        )
            