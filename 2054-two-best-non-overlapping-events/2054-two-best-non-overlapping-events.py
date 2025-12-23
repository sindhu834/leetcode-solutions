class Solution:
    def maxTwoEvents(self, events):
        # Sort events by start time
        events.sort(key=lambda x: x[0])

        # Create list sorted by end time
        ends = sorted([(end, value) for start, end, value in events])

        max_value_so_far = 0
        ans = 0
        j = 0  # pointer for ended events

        for start, end, value in events:
            # Update max_value_so_far for events that end before this start
            while j < len(ends) and ends[j][0] < start:
                max_value_so_far = max(max_value_so_far, ends[j][1])
                j += 1

            # Take current event + best previous event
            ans = max(ans, value + max_value_so_far)

        return ans
