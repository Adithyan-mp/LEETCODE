class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert to a max-heap by inverting the values (negative sign)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)  # O(n) to heapify the list

        score = 0
        for i in range(k):
            # Get the maximum element by popping from the heap
            max_val = -heapq.heappop(max_heap)
            score += max_val
            
            # Push the updated value back into the heap (ceil(max_val / 3))
            heapq.heappush(max_heap, -ceil(max_val / 3))

        return score