"""
Module for Competitions - Strategy pattern.
"""

from CompetitionBehaviours.displayLeaderboard.displayText import \
    displayLeaderboardBehaviour as defaultDisplayBehaviour

from CompetitionBehaviours.distributePrizes.equitable import \
    distributePrizesBehaviour as defaultPrizeBehaviour

from CompetitionBehaviours.scoreParticipant.get_score import \
    scoreParticipantBehaviour as defaultScoreParticipantBehaviour


class Competition(object):

    def __init__(self, distributePrizesBehaviour=None,
                 displayLeaderboardBehaviour=None,
                 scoreParticipantBehaviour=None):
        """
        :param distributePrizesBehaviour: Interface for something which can distributePrizes
        :param displayLeaderboardBehaviour: Interface for something to displayLeaderboard
        :param scoreParticipantBehaviour: Interface to scoreParticipant, used for sorting (in reverse)
        """
        self.participants = []

        self._distributePrizesBehaviour = distributePrizesBehaviour or \
                                          defaultPrizeBehaviour
        self.distributePrizesBehaviour = self._distributePrizesBehaviour()
        
        self._displayLeaderboardBehaviour = displayLeaderboardBehaviour or \
                                            defaultDisplayBehaviour
        self.displayLeaderboardBehaviour = self._displayLeaderboardBehaviour()

        self._scoreParticipantBehaviour = scoreParticipantBehaviour or \
                                          defaultScoreParticipantBehaviour
        self.scoreParticipantBehaviour = self._scoreParticipantBehaviour()

    def addParticipant(self, participant):
        if self.getParticipant(participant) is None:
            self.participants.append(participant)
            return True
        else:
            return False

    def getParticipant(self, participant):
        result = filter(lambda p: p == participant,
                        self.participants)
        try:
            return result[0]
        except IndexError:
            return None

    def listParticipants(self, ordered=False):  # todo: filter=None
        if ordered:
            return sorted(self.participants, reverse=True,
                          key=lambda p: \
                          self.scoreParticipantBehaviour.scoreParticipant(p) or 0)
        else:
            return self.participants

    def setPrize(self, prize_map):
        self.prize_map = prize_map

    def seePrize(self):
        return "The prize is " + str(self.getPrize())

    def getPrize(self):
        try:
            return self.prize_map
        except AttributeError:
            return None
    
    def distributePrizes(self):
        self.distributePrizesBehaviour.distributePrizes(self)  # pass in the Comp

    def displayLeaderboard(self):
        self.displayLeaderboardBehaviour.displayLeaderboard(self)  # pass the Comp

    def scoreParticipant(self, participant):
        self.scoreParticipantBehaviour.scoreParticipant(self, participant)
