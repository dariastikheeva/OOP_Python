class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2
        self.d = self.clock1.get_time() - self.clock2.get_time() # difference in seconds

    def __str__(self):
        if self.d < 0:
            return f'00: 00: 00'
        h = self.d // 3600
        m = (self.d - h * 3600) // 60
        s = self.d - h * 3600 - m * 60
        return f'{h:02}: {m:02}: {s:02}'
    
    def __len__(self):
        return self.d

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
