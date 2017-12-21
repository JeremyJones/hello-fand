class Participant(object):
    def __init__(self, name, score):
        """

        :param name: string
        :param score: integer
        """
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_prize(self):
        try:
            return self.prize
        except AttributeError:
            return None

    def set_prize(self, prize):
        """

        :param prize: integer
        """
        self.prize = prize


def sort_participants(participants):
    pass


def distribute_prizes(participants, prizes):
    pass
