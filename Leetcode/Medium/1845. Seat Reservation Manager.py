"""
1845. Seat Reservation Manager
(Medium complexity)

Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
"""


class SeatManager:

    def __init__(self, n: int):
        self.not_reserved = []
        self.last = 0

    def reserve(self) -> int:
        if not self.not_reserved:
            self.last += 1
            return self.last
        return heapq.heappop(self.not_reserved)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber != self.last:
            heapq.heappush(self.not_reserved, seatNumber)
        else:
            self.last -= 1


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)