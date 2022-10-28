# Checked Date: 2022/10/27

# You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:
#
# event1 = [startTime1, endTime1] and
# event2 = [startTime2, endTime2].
# Event times are valid 24 hours format in the form of HH:MM.
#
# A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
#
# Return true if there is a conflict between two events. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
# Output: true
# Explanation: The two events intersect at time 2:00.


# Example 2:
#
# Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
# Output: true
# Explanation: The two events intersect starting from 01:20 to 02:00.


# Example 3:
#
# Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
# Output: false
# Explanation: The two events do not intersect.
#
#
# Constraints:
#
# evnet1.length == event2.length == 2.
# event1[i].length == event2[i].length == 5
# startTime1 <= endTime1
# startTime2 <= endTime2
# All the event times follow the HH:MM format.

from typing import List


def haveConflict(event1: List[str], event2: List[str]) -> bool:
    startTime1 = int(event1[0].split(":")[0])+int(event1[0].split(":")[1])/60
    endTime1 = int(event1[1].split(":")[0])+int(event1[1].split(":")[1])/60
    startTime2 = int(event2[0].split(":")[0]) + int(event2[0].split(":")[1]) / 60
    endTime2 = int(event2[1].split(":")[0]) + int(event2[1].split(":")[1]) / 60
    if startTime2 <= startTime1 <= endTime2 or startTime1 <= startTime2 <= endTime1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]))
