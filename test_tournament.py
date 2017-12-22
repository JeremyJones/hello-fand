from unittest import TestCase

from tournament import Participant, distribute_prizes, sort_participants


class ParticipantTestCase(TestCase):
    def setUp(self):
        self.steve = Participant('Steve', 100)

    def test_participant_constructor(self):
        self.assertEqual(self.steve.get_name(), 'Steve')
        self.assertEqual(self.steve.get_score(), 100)
        self.assertEqual(self.steve.get_prize(), None)

    def test_participant_set_prize(self):
        self.assertEqual(self.steve.get_prize(), None)

        self.steve.set_prize(55)

        self.assertEqual(self.steve.get_prize(), 55)


class ParticipantSortTestCase(TestCase):
    def setUp(self):
        # self.skipTest("Part II")

        self.abby = Participant('Abby', 100)
        self.bill = Participant('Bill', 80)
        self.carl = Participant('Carl', 60)
        self.dave = Participant('Dave', 40)

    def test_sort_participants(self):
        self.assertEqual(
            sort_participants(
                [self.abby, self.bill, self.carl, self.dave]
            ),
            [self.abby, self.bill, self.carl, self.dave]
        )

    def test_sort_participants_two(self):
        self.assertEqual(
            sort_participants(
                [self.carl, self.abby, self.dave, self.bill]
            ),
            [self.abby, self.bill, self.carl, self.dave]
        )

    def test_sort_participants_three(self):
        self.assertEqual(
            sort_participants(
                [self.dave, self.bill]
            ),
            [self.bill, self.dave]
        )


class DistributePrizesTestCase(TestCase):
    def setUp(self):
        # self.skipTest("Parts III & IV")

        self.prizes = {
            1: 50,
            2: 20,
            3: 10,
        }

    def test_example_one(self):
        self.sally = Participant('Sally', 77)
        self.betty = Participant('Betty', 66)
        self.don = Participant('Don', 46)
        self.megan = Participant('Megan', 45)

        distribute_prizes(sort_participants(
            [self.megan, self.don, self.betty, self.sally]),
            self.prizes)

        self.assertEqual(
            [self.sally,     self.sally.get_prize(),
             self.betty,     self.betty.get_prize(),
             self.don,       self.don.get_prize(),
             self.megan,     self.megan.get_prize()],

            [self.sally,     50,
             self.betty,     20,
             self.don,       10,
             self.megan,      0]
        )

    def test_example_two(self):
        self.roger = Participant('Roger', 77)
        self.jane = Participant('Jane', 66)
        self.pete = Participant('Pete', 45)
        self.cooper = Participant('Cooper', 45)

        distribute_prizes(sort_participants(
            [self.roger, self.jane, self.pete, self.cooper]),
            self.prizes)

        self.assertEqual(
            [self.roger,      self.roger.get_prize(),
             self.jane,       self.jane.get_prize(),
             self.pete,       self.pete.get_prize(),
             self.cooper,     self.cooper.get_prize()],

            [self.roger,      50,
             self.jane,       20,
             self.pete,        5,
             self.cooper,      5]
        )

    def test_example_three(self):
        self.peggy = Participant('Peggy', 77)
        self.tom = Participant('Tom', 66)
        self.joan = Participant('Joan', 66)
        self.ken = Participant('Ken', 45)

        distribute_prizes(sort_participants(
            [self.peggy, self.tom, self.joan, self.ken]),
            self.prizes)

        self.assertEqual(
            [self.peggy,       self.peggy.get_prize(),
             self.tom,         self.tom.get_prize(),
             self.joan,        self.joan.get_prize(),
             self.ken,         self.ken.get_prize()],

            [self.peggy,       50,
             self.tom,         15,
             self.joan,        15,
             self.ken,          0]
        )

    def test_example_four(self):
        self.harry = Participant('Harry', 77)
        self.lane = Participant('Lane', 45)
        self.stan = Participant('Stan', 45)
        self.henry = Participant('Henry', 45)

        distribute_prizes(sort_participants(
            [self.harry, self.lane, self.stan, self.henry]),
            self.prizes)

        self.assertEqual(
            [self.harry,        self.harry.get_prize(),
             self.lane,         self.lane.get_prize(),
             self.stan,         self.stan.get_prize(),
             self.henry,        self.henry.get_prize()],

            [self.harry,        50,
             self.lane,         10,
             self.stan,         10,
             self.henry,        10]
        )

    def test_example_five(self):
        self.ted = Participant('Ted', 77)
        self.trudy = Participant('Trudy', 77)
        self.bobby = Participant('Bobby', 46)
        self.paul = Participant('Paul', 46)

        distribute_prizes(sort_participants(
            [self.ted, self.trudy, self.bobby, self.paul]),
            self.prizes)

        self.assertEqual(
            [self.ted,           self.ted.get_prize(),
             self.trudy,         self.trudy.get_prize(),
             self.bobby,         self.bobby.get_prize(),
             self.paul,          self.paul.get_prize()],

            [self.ted,           35,
             self.trudy,         35,
             self.bobby,          5,
             self.paul,           5]
        )
