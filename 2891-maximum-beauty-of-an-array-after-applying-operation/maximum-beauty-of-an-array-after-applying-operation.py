class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num - k, 1))  # Start of range
            events.append((num + k + 1, -1))  # End of range (exclusive)

        # Sort events by value, and in case of tie, by type of event
        events.sort()

        # Use a sweep line approach to calculate the maximum overlap
        max_beauty = 0
        current_count = 0
        for value, effect in events:
            current_count += effect
            max_beauty = max(max_beauty, current_count)

        return max_beauty
