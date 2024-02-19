"""
2402. Meeting Rooms III
(Hard complexity)

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.
"""


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()

        count = [0] * n
        heap_meat = []
        unused = [i for i in range(n)]

        for i in range(m):
            while heap_meat and heap_meat[0][0] <= meetings[i][0]:
                free_room = heapq.heappop(heap_meat)
                heapq.heappush(unused, free_room[1])

            if unused:
                cur_room = heapq.heappop(unused)
                heapq.heappush(heap_meat, (meetings[i][1], cur_room))
            else:
                end_time, cur_room = heapq.heappop(heap_meat)
                diff = meetings[i][1] - meetings[i][0]
                heapq.heappush(heap_meat, (end_time + diff, cur_room))
            count[cur_room] += 1

        return count.index(max(count))