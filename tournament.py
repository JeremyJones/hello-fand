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
        Set a specific prize, REPLACING any previous prize.
        :param prize: integer
        """
        self.prize = prize


def sort_participants(participants):
    """
    Sort a list of Participant objects by their score, in descending order.
    :param participants: list
    :return: list
    """
    return sorted(participants, key=lambda p: p.get_score() or 0, reverse=True)


def distribute_prizes(participants, prizes):
    """
    Updates list of winners with their prize values, in-place.
    :param participants: sorted list of Participant objects
    :param prizes: map of prize values
    :return: None
    """
    for pidx in range(len(participants)):
        if pidx + 1 in prizes:
            prize = prizes[pidx + 1]
            del(prizes[pidx + 1])

            myscore = participants[pidx].get_score()

            winners = [pidx]  # there might be more than one. remember the idx
            nextPerson = pidx + 1

            for additionalidx in range(nextPerson, len(participants)):
                if participants[additionalidx].get_score() == myscore:
                    winners.append(additionalidx)  # they also win

                    if additionalidx + 1 in prizes:  # and there's more money
                        prize += prizes[additionalidx + 1]
                        del(prizes[additionalidx + 1])
                else:
                    break

            for winner in winners:
                participants[winner].set_prize(prize / len(winners))

        elif participants[pidx].get_prize() is None:
            participants[pidx].set_prize(0)
