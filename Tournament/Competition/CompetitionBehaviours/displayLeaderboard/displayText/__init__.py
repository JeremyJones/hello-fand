"""
Behaviour class to implement displayLeaderboard()

Print a simple text string table with competition results to stdout.
"""

class displayLeaderboardBehaviour(object):

    def displayLeaderboard(self, comp):

        def prize_or_none(prize):
            if prize is None:
                return 'None'
            else:
                return '${}'.format(prize)
            
        
        output = "{lines}\n{headers}\n{lines}\n{people}\n{lines}".\
                 format(
                     lines="+".join(['',
                                     ''.join(['-']*(len('Participant')+2)),
                                     ''.join(['-']*(len('Score')+2)),
                                     ''.join(['-']*(len('Prize')+2)),
                                     '']),
                     headers="|".join(['',
                                       ' Participant ', ' Score ', ' Prize ',
                                       '']),
                     people="\n".\
                     join(map(lambda p: '| %-12s| %5d | %5s |' % (p.get_name(), p.get_score(),
                                                                  prize_or_none(p.get_prize())),
                              comp.listParticipants(ordered=True))))

        print output
