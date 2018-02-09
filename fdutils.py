def next_winner(participants, winningScore):
    for p in participants:
        if p.get_score() == winningScore:
            yield p