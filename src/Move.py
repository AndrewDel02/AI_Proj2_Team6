class Move:
    def __init__(self, location, turn_player):
        self.location = location
        self.turn_player = turn_player

    def convert_location_to_ref_representation(self):
        """Converts move from board config to referee format as a string"""
        if self.location == -1:
            return "P0"
        column = chr(self.location % 8 + 65)  # columns are A-H
        row = str(int(self.location/8) + 1)  # rows are 1-8
        return column + " " + row

