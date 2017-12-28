class scoreParticipantBehaviour(object):

    def scoreParticipant(self, participant):
        """
        Longest participant name score behaviour
        """
        return len(participant.get_name())
