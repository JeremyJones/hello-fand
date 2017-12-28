class distributePrizesBehaviour(object):

    def distributePrizes(self, comp):
        """
        Longest name prize distribution behaviour
        """
        participants = sorted(comp.listParticipants(ordered=False),
                              reverse=True,
                              key=lambda p: len(p.get_name()))
        prizes = comp.getPrize()

        for pidx in range(len(participants)):
            if pidx + 1 in prizes:
                prize = prizes[pidx + 1]
                del(prizes[pidx + 1])
                
                myscore = len(participants[pidx].get_name())
                
                winners = [pidx]  # there might be more than one. remember the idx
                nextPerson = pidx + 1

                for additionalidx in range(nextPerson, len(participants)):
                    if len(participants[additionalidx].get_name()) == myscore:
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
