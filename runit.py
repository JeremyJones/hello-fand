"""

"""

from Competition import Competition
from Participant import Participant



def main():
    c = Competition()

    prize_map = {1: 50, 2: 20, 3: 10}
    c.setPrize(prize_map)

    for p in [['John',20],['Paul',10],['George',3],['Ringo',None]]:
        participant = Participant(p[0],p[1])
        c.addParticipant(participant)


    c.displayLeaderboard()


if __name__ == "__main__":
    main()
