"""
Class for Participants
"""

class Participant(object):
    def __init__(self, name, score=None):

        self.set_name(name)

        if score is not None:
            self.set_score(score)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
    def set_score(self, score):
        self.score = score

    def get_score(self):
        try:
            return self.score
        except AttributeError:
            return 0

    def set_prize(self, prize):
        self.prize = prize

    def get_prize(self):
        try:
            return self.prize
        except AttributeError:
            return None

    def summarise(self):
        return "{name}: {score} ({prize})".\
            format(name=self.get_name(),
                   score=self.get_score(),
                   prize=self.get_prize())
