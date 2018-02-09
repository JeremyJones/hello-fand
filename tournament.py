from collections import OrderedDict
from fdutils import next_winner


class PrizeMap(OrderedDict):
    def next_prize(self):
        for prize in self.values():
            yield prize


class Participant():
    def __init__(self, name, score) -> None:
        """
        :param name: string
        :param score: integer
        """
        self.name = name
        self.score = score

    def get_name(self) -> str:
        return self.name

    def get_score(self) -> int:
        return self.score

    def get_prize(self):
        try:
            return self.prize
        except AttributeError:
            return None

    def set_prize(self, prize) -> None:
        """
        Set a specific prize, REPLACING any previous prize.
        :param prize: integer
        """
        self.prize = prize


def sort_participants(participants):
    """
    Sort a list of Participant objects by their score, in descending order.
    :param participants: list
    :return: iterable
    """
    return sorted(participants, key=lambda p: p.get_score() or 0,
                  reverse=True)


def distribute_prizes(participants, prizes: PrizeMap) -> None:
    """
    Updates list of winners with their prize values, in-place.
    :param participants: sorted list of Participant objects
    :param prizes: map of prize values
    :return: None
    """
    for p in participants:

        if p.get_prize() is not None:
            continue
        else:
            mywinners, myprizes = [], []

            for winner, prize in zip(next_winner(participants,
                                                 p.get_score()),
                                     prizes.next_prize()):
                mywinners.append(winner)
                myprizes.append(prize)

            for winner in mywinners:
                winner.set_prize(sum(myprizes) / len(mywinners))
