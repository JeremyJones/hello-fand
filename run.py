"""

"""

# core objects:
#
from Tournament.Competition import Competition
from Tournament.Participant import Participant

# sample data:
#
from Tournament.SampleData import (example_prize_map as prize_map_old,
                                   longer_prize_map as prize_map,
                                   beatles as participants_previous,
                                   planets as participants,
                                   )

# built-in optional behaviour overrides:
#
from Tournament.Competition.CompetitionBehaviours.displayLeaderboard.displayHTML \
    import displayLeaderboardBehaviour as displayHTML
#
from Tournament.Competition.CompetitionBehaviours.scoreParticipant.longest_name \
    import scoreParticipantBehaviour as longestNameWins


def main():
    c = Competition()

    # examples of other possibilities:
    #
    # c = Competition(#displayLeaderboardBehaviour=displayHTML,
    #                 scoreParticipantBehaviour=longestNameWins)
    #
    c.setPrize(prize_map)

    for p in participants:
        participant = Participant(p[0],p[1])
        c.addParticipant(participant)

    c.distributePrizes()
    c.displayLeaderboard()


if __name__ == "__main__":
    main()
