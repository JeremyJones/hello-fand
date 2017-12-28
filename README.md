# FanDuel Python homework problem - dp_strategy

This branch contains revisions to the code reflecting the *Strategy*
Design Pattern.

With this revision, objects for Competition and Participant have been
split into separate files, and within the Competition object the
algorithms for the functions below have been encapsulated, allowing
them to be interchanged in orderto affect their behaviour:

* distributePrizes
* displayLeaderboard

The current Behaviours behind the interfaces are the defaults as
provided in the main task description.


# FanDuel Python homework problem

In a tournament, prizes are distributed among the top P positions in
a tournament of Q participants. Participants are awarded a prize based on their
score (higher is better). In the case where two or more participants have the
same score, each participant receives an equal share of the prizes for the
positions they cover. For example, if the top two players have the same score,
they cover the positions 1 & 2, and they split the prizes for positions
1 & 2 equally.


## Examples

Given the following prizes:

* First prize $50;
* Second prize $20;
* Third prize $10.

The following participants in each tournament would receive the prizes
described.


### Example 1

    +-------------+-------+-------+
    | Participant | Score | Prize |
    +-------------+-------+-------+
    | Sally       |    77 |   $50 |
    | Betty       |    66 |   $20 |
    | Don         |    46 |   $10 |
    | Megan       |    45 |    $0 |
    +-------------+-------+-------+


### Example 2

    +-------------+-------+-------+
    | Participant | Score | Prize |
    +-------------+-------+-------+
    | Roger       |    77 |   $50 |
    | Jane        |    66 |   $20 |
    | Pete        |    45 |    $5 |
    | Cooper      |    45 |    $5 |
    +-------------+-------+-------+


### Example 3

    +-------------+-------+-------+
    | Participant | Score | Prize |
    +-------------+-------+-------+
    | Peggy       |    77 |   $50 |
    | Tom         |    66 |   $15 |
    | Joan        |    66 |   $15 |
    | Ken         |    45 |    $0 |
    +-------------+-------+-------+


### Example 4

    +-------------+-------+-------+
    | Participant | Score | Prize |
    +-------------+-------+-------+
    | Harry       |    77 |   $50 |
    | Lane        |    45 |   $10 |
    | Stan        |    45 |   $10 |
    | Henry       |    45 |   $10 |
    +-------------+-------+-------+


### Example 5

    +-------------+-------+-------+
    | Participant | Score | Prize |
    +-------------+-------+-------+
    | Ted         |    77 |   $35 |
    | Trudy       |    77 |   $35 |
    | Bobby       |    46 |    $5 |
    | Paul        |    46 |    $5 |
    +-------------+-------+-------+


## Tasks


### Part I

Complete the implementation of the class `Participant`, as outlined in
`tournament.py`, so that it passes the tests in `ParticipantTestCase` (in
`test_tournament.py`).

The unit–tests can be run with:

    python -m unittest discover

Feel free to use either Python 2, or 3.


### Part II

Sort a list of `Participant` objects by their score, in descending order, so
that it passes the tests in `ParticipantSortTestCase` (remove the `skipTest`
line in `setUp`).


### Part III

Implement a function `distribute_prizes`, which takes a list of `Participant`
objects, and a “prize–map” dictionary, of the following form:

    prizes = {
        <position>: <prize>,
        <position>: <prize>,
        <position>: <prize>,
        …
    }

The “prize–map” for the example above would be:

    prizes = {
        1: 50,
        2: 20,
        3: 10,
    }


### Part IV

Write five unit–tests, reflecting the above examples, to demonstrate your
implementation of `distribute_prizes` working as expected.

