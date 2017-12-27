"""
Module for Competitions - Strategy pattern.
"""

from CompetitionBehaviours.Default.distributePrizes import \
    distributePrizesBehaviour as defaultPrizeBehaviour

from CompetitionBehaviours.Default.displayLeaderboard import \
    displayLeaderboardBehaviour as defaultDisplayBehaviour

class Competition(object):

    def __init__(self, distributePrizesBehaviour=None,
                 displayLeaderboardBehaviour=None):
        """
        :param distributePrizesBehaviour: Interface for something which can distributePrizes
        :param displayLeaderboardBehaviour: Interface for something to displayLeaderboard
        """
        self.participants = []

        self._distributePrizesBehaviour = distributePrizesBehaviour or \
                                          defaultPrizeBehaviour
        self.distributePrizesBehaviour = self._distributePrizesBehaviour()
        
        self._displayLeaderboardBehaviour = displayLeaderboardBehaviour or \
                                            defaultDisplayBehaviour
        self.displayLeaderboardBehaviour = self._displayLeaderboardBehaviour()
        
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

    def listParticipants(self):  # todo: filter=None
        return self.participants

    def setPrize(self, prize_map):
        self.prize_map = prize_map

    def seePrize(self):
        return "The prize is " + str(self.getPrize())

    def getPrize(self):
        try:
            return self.prize_map
        except StandardError:  # todo, limit this error 
            #return None
            raise
    
    def distributePrizes(self):
        self.distributePrizesBehaviour.distributePrizes(self)  # pass in the Comp

    def displayLeaderboard(self):
        self.displayLeaderboardBehaviour.displayLeaderboard(self)  # pass the Comp
