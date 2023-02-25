# https://leetcode.com/problems/minimize-deviation-in-array/submissions/904666520/

from heapq import heappush, heappop


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minimum_element = 10 ** 9 + 1
        heap = []

        for current_element in nums:
            if current_element % 2 == 1:
                current_element *= 2

            minimum_element = min(minimum_element, current_element)
            heappush(heap, -current_element)

        minimum_deviation = 10 ** 9
        while True:
            maximum_element = -heappop(heap)
            minimum_deviation = min(minimum_deviation, maximum_element - minimum_element)

            if maximum_element % 2 == 1:
                break

            maximum_element //= 2
            minimum_element = min(minimum_element, maximum_element)
            heappush(heap, -maximum_element)

        return minimum_deviation
