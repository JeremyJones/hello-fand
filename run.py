"""

"""

# core objects:
#
from Tournament.Competition import Competition
from Tournament.Participant import Participant

# sample data:
#
from Tournament.SampleData import (example_prize_map as prize_map,
                                   beatles as participants)

# optional behaviour overrides:
#
# from Tournament.Competition.CompetitionBehaviours.displayLeaderboard.displayHTML \
#     import displayLeaderboardBehaviour as displayHTML
#
# from Tournament.Competition.CompetitionBehaviours.distributePrizes.longest_name \
##    import distributePrizesBehaviour as awardByNameLength


def main():
    c = Competition()

    # other options:
    #
    # Competition(displayLeaderboardBehaviour=displayHTML)
    # Competition(distributePrizesBehaviour=awardByNameLength)

    c.setPrize(prize_map)

    for p in participants:
        participant = Participant(p[0],p[1])
        c.addParticipant(participant)

    c.distributePrizes()
    c.displayLeaderboard()


if __name__ == "__main__":
    main()
