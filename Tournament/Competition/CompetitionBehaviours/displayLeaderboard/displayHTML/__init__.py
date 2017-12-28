"""
Behaviour class to implement displayLeaderboard()

Print an HTML table with competition results to stdout.
"""

class displayLeaderboardBehaviour(object):

    def displayLeaderboard(self, comp):

        def prize_or_none(prize):
            if prize is None:
                return 'None'
            else:
                return '${}'.format(prize)
            
        
        output = "<table><tr><th>Participant</th>" + \
                 "<th>Score</th><th>Prize</th></tr>" + \
                 ''.join(map(lambda p: \
                             '<tr><td>%s</td><td align=right>%d</td><td align=right>%s</td></tr>' % \
                             (p.get_name(), p.get_score(), prize_or_none(p.get_prize())),
                             comp.listParticipants(ordered=True))) + \
                 "</table>"

        print output
