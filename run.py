from tournament import (Participant, PrizeMap, distribute_prizes,      
                        sort_participants)


def main() -> None:
    p = PrizeMap({"1": 100, "2": 50, "3": 25})
    
    players = sort_participants([
               Participant('John', 20), Participant('Jack', 50),
               Participant('Tom', 10), Participant('Andy', 24)
               ])

    distribute_prizes(players, p)

    for p in players:
        print("{name} scored {score} and won {prize}.".\
              format(name=p.get_name(), score=p.get_score(),
                     prize=p.get_prize()))


if __name__ == '__main__':
    main()