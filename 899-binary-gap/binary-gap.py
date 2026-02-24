class Solution:
    def binaryGap(self, n: int) -> int:
        last_pos = None
        max_gap = 0
        current_pos = 0
        
        while n > 0:
            # Check if the current bit is 1
            if n & 1:
                if last_pos is not None:
                    # Update max_gap with the distance from the previous 1
                    max_gap = max(max_gap, current_pos - last_pos)
                last_pos = current_pos
            
            # Move to the next bit
            n >>= 1
            current_pos += 1
            
        return max_gap