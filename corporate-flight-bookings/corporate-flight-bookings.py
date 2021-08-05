class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for first, last, seats in bookings:
            diff[first-1] += seats
            j = last
            if j < n:
                diff[j] -= seats
        ret = [0] * n
        ret[0] = diff[0]
        for i in range(1,n):
            ret[i] = ret[i-1] + diff[i]
        return ret
        