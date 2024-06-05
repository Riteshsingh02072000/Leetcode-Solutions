class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        meetings.sort(key = lambda x:x[0])
        new_meeting = []
        cur_start, cur_end = meetings[0]

        for start, end in meetings[1:]:
            if start<=cur_end:
                cur_end = max(cur_end, end)
            else:
                new_meeting.append([cur_start, cur_end])
                cur_start, cur_end = start, end
        
        new_meeting.append([cur_start, cur_end])
        working_days = sum(end-start+1 for start, end in new_meeting)
        return days-working_days