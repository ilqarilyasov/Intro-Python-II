# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.e_to = None
        self.w_to = None
        self.n_to = None
        self.s_to = None

    def __repr__(self):
        return f"{self.name}, {self.description}"
