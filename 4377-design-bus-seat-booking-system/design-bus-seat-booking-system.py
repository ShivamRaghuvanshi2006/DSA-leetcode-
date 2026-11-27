class BusBooking:
    def __init__(self, n: int):
        self.booked = {}  # seat -> cost
        self.total = 0

    def toggle(self, seat: str) -> None:
        if seat in self.booked:
            self.total -= self.booked.pop(seat)
            return
        letter = seat[0]
        rownum = seat[1:]
        if letter == 'B' or letter == 'C':
            cost = 1
        else:
            adj = ('B' + rownum) if letter == 'A' else ('C' + rownum)
            cost = 3 if adj in self.booked else 1
        self.booked[seat] = cost
        self.total += cost

    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return len(self.booked)