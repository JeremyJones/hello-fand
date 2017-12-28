"""

"""

# core objects:
#
from Tournament.Competition import Competition
from Tournament.Participant import Participant

# sample data:
#
from Tournament.SampleData.prize_maps import example_prize_map
from Tournament.SampleData.participants import beatles

# optional behaviour overrides:
#
# from Competition.CompetitionBehaviours.displayLeaderboard.displayHTML \
#     import displayLeaderboardBehaviour as displayHTML


def main():
    c = Competition()  # or e.g. Competition(displayLeaderboardBehaviour=displayHTML)

    c.setPrize(example_prize_map)

    for p in beatles:
        participant = Participant(p[0],p[1])
        c.addParticipant(participant)

    c.displayLeaderboard()


if __name__ == "__main__":
    main()
