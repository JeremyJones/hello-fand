from tournament import (Participant, PrizeMap, distribute_prizes,      
                        sort_participants)


""" Helpers for interactive mode.
"""
jer = Participant('Jer',100)
john = Participant('John', 30)
prizes = PrizeMap({"1": 100, "2": 60, "3": 40})

distribute_prizes([jer, john], prizes)
