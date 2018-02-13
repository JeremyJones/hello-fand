from collections import OrderedDict


def next_winner(participants, winningScore):
    """ generator for grepping players who have a particular score
    """
    for p in participants:
        if p.get_score() == winningScore:
            yield p


class PrizeMap(OrderedDict):
    prizes = None

    def next_prize(self):

        if self.prizes is None:
            self.prizes = self.values()

        for prize in self.prizes:
            yield prize


class PodiumPlace(list):
    pass


class Participant:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return "Participant('{n}', {s}).set_prize({p})".\
                format(n=self.get_name(), s=self.get_score(),
                       p=self.get_prize())

    def __len__(self) -> int:
        return self.get_score()

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
        Set a specific prize, replacing any previous prize.
        """
        self.prize = prize


def sort_participants(participants):
    """
    Sort a list of Participant objects by their score, in descending order.
    :param participants: list
    :return: iterable
    """
    return sorted(participants, key=len, reverse=True)


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
            winners, prize_money = PodiumPlace(), 0

            for winner, prize in zip(next_winner(participants,
                                                 p.get_score()),
                                     prizes.next_prize()):
                winners.append(winner)
                prize_money += prize

            if prize_money == 0:
                break

            for winner in winners:
                winner.set_prize(prize_money / len(winners))
