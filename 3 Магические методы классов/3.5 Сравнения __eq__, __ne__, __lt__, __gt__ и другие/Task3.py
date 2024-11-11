import math

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    def length(self, from_x, from_y):
        return math.sqrt(math.pow(self.to_x - from_x, 2) + math.pow(self.to_y - from_y, 2))

class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def add_track(self, tr):
        self.tracks.append(tr)

    def get_tracks(self):
        return tuple(self.tracks)

    def get_length(self):
        total_length = 0
        current_x, current_y = self.start_x, self.start_y
        
        for i in self.tracks:
            total_length += i.length(current_x, current_y)
            current_x, current_y = i.to_x, i.to_y
            
        return total_length

    def __eq__(self, other):
        return self.get_length() == other.get_length()

    def __ne__(self, other):
        return self.get_length() != other.get_length()

    def __gt__(self, other):
        return self.get_length() > other.get_length()

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __len__(self):
        return int(self.get_length())

track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
