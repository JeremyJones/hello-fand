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
        Set a specific prize. Doesn't add prizes.
        :param prize: integer
        """
        self.prize = prize


def sort_participants(participants):
    """
    Sort a list of Participant objects by their score, in descending order.
    :param participants: list
    :return: list
    """
    return sorted(participants, key=lambda _: _.get_score() or 0, reverse=True)


def distribute_prizes(participants, prizes):
    pass
