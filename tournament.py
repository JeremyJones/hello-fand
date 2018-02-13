from collections import OrderedDict


def next_winner(participants, winningScore):
    for p in participants:
        if p.get_score() == winningScore:
            yield p


class PrizeMap(OrderedDict):
    prizes = None

    def next_prize(self):

        if self.prizes is None:
            self.prizes = self.values()

        for prize in prizes:
            yield prize


class Participant:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return "Participant('{n}', {s})".format(n=self.name, s=self.score)

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
            mywinners, prize_money = [], 0

            for winner, prize in zip(next_winner(participants,
                                                 p.get_score()),
                                     prizes.next_prize()):
                mywinners.append(winner)
                prize_money += prize

            for winner in mywinners:
                winner.set_prize(prize_money / len(mywinners))


""" Helpers for interactive mode.
"""
jer = Participant('Jer',100)
john = Participant('John', 30)
prizes = PrizeMap({"1": 100, "2": 60, "3": 40})
