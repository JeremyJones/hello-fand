class distributePrizesBehaviour(object):

    def distributePrizes(self, comp):
        """
        Equitable prize distribution behaviour

        Participants are awarded a prize based on their score (higher
        is better). In the case where two or more participants have
        the same score, each participant receives an equal share of
        the prizes for the positions they cover. For example, if the
        top two players have the same score, they cover the positions
        1 & 2, and they split the prizes for positions 1 & 2 equally.
        """
        participants = comp.listParticipants(ordered=True)
        prizes = comp.getPrize()

        if not prizes:
            raise RuntimeError("No prizes defined")

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
