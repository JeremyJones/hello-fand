from collections import OrderedDict
from operator import attrgetter
from fdutils import num_winners
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
    for pidx, participant in enumerate(participants):

        if participant.get_prize() is not None:
            continue
        elif prizes.get(pidx + 1) is None:
            participant.set_prize(0)
        else:
            mwinners, mprizes = [], []

            for winner, prize in zip(next_winner(participants,
                                                 participant.get_score()),
                                     prizes.next_prize()):
                mwinners.append(winner)
                mprizes.append(prize)

            for winner in mwinners:
                winner.set_prize(sum(mprizes) / len(mwinners))
