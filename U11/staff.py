"""
Staff class
@author: GK
"""

class Staff():
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        
    def __repr__(self):
        return f'{self.name} works for {self.hours} hours'