'''
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap.
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation: There is no meeting scheduled on the 4th and 8th days.

sorted(meetings, key=lambda x:x[1])
'''


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        # Sort the meeting based on start day.
        meetings = sorted(meetings, key=lambda x: x[0])
        meetings_count = 0
        n = len(meetings)
        start = meetings[0][0]
        end = meetings[0][1]
        print(meetings)
        for i in range(1, n):
            # Overlapping meeting, reset the end to current one.
            # print(meetings[i])
            if (end < meetings[i][0]):
                meetings_count += (end - start) + 1
                # print(f"Loop {end} - {start} Meeting count {meetings_count}")
                start = meetings[i][0]
                end = meetings[i][1]
            elif (start <= meetings[i][0] and end <= meetings[i][1]):
                # print("Update endpoint")
                end = meetings[i][1]

        meetings_count += (end - start) + 1
        # print(f"{end} - {start} Meeting count {meetings_count}")
        return days - meetings_count


if __name__ == "__main__":
    s = Solution()
    days = 10
    meetings = [[5, 7], [1, 3], [9, 10]]
    print(
        f"meeting {meetings} and days={days} the number of non-meeting days {s.countDays(days, meetings)}")

    days = 8
    meetings = [[3, 4], [4, 8], [2, 5], [3, 8]]
    print(
        f"meeting {meetings} and days={days} the number of non-meeting days {s.countDays(days, meetings)}")

    days = 57
    meetings = [[3, 49], [23, 44], [21, 56], [
        26, 55], [23, 52], [2, 9], [1, 48], [3, 31]]
    print(
        f"meeting {meetings} and days={days} the number of non-meeting days {s.countDays(days, meetings)}")
