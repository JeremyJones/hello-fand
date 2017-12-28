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
# from Competition.CompetitionBehaviours.displayLeaderboard.displayHTML \
#     import displayLeaderboardBehaviour as displayHTML


def main():
    c = Competition()  # or e.g. Competition(displayLeaderboardBehaviour=displayHTML)

    c.setPrize(prize_map)

    for p in participants:
        participant = Participant(p[0],p[1])
        c.addParticipant(participant)

    c.displayLeaderboard()


if __name__ == "__main__":
    main()
