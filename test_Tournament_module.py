from unittest import main,TestCase

from Tournament.Competition import Competition
from Tournament.Participant import Participant
#from tournament import Participant, distribute_prizes, sort_participants


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

        c = Competition()

        self.abby = Participant('Abby', 100)
        self.bill = Participant('Bill', 80)
        self.carl = Participant('Carl', 60)
        self.dave = Participant('Dave', 40)
        self.comp = Competition()

        

    def test_sort_participants(self):
        self.comp.addParticipant(self.abby)
        self.comp.addParticipant(self.bill)
        self.comp.addParticipant(self.carl)
        self.comp.addParticipant(self.dave)

        sorted_list = self.comp.listParticipants(ordered=True)
        
        self.assertEqual(sorted_list,
            [self.abby, self.bill, self.carl, self.dave]
        )

    def test_sort_participants_two(self):
        # self.skipTest("2.2")
        
        self.comp.addParticipant(self.carl)
        self.comp.addParticipant(self.abby)
        self.comp.addParticipant(self.dave)
        self.comp.addParticipant(self.bill)

        sorted_list = self.comp.listParticipants(ordered=True)

        self.assertEqual(sorted_list,
            [self.abby, self.bill, self.carl, self.dave]
        )

    def test_sort_participants_three(self):
        # self.skipTest("2.3")

        self.comp.addParticipant(self.dave)
        self.comp.addParticipant(self.bill)

        sorted_list = self.comp.listParticipants(ordered=True)

        self.assertEqual(sorted_list,
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

        self.comp = Competition()
        self.comp.setPrize(self.prizes)

    def test_example_one(self):
        self.sally = Participant('Sally', 77)
        self.betty = Participant('Betty', 66)
        self.don = Participant('Don', 46)
        self.megan = Participant('Megan', 45)

        self.comp.addParticipant(self.sally)
        self.comp.addParticipant(self.betty)
        self.comp.addParticipant(self.don)
        self.comp.addParticipant(self.megan)

        self.comp.distributePrizes()

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
        # self.skipTest("Parts III & IV")

        self.roger = Participant('Roger', 77)
        self.jane = Participant('Jane', 66)
        self.pete = Participant('Pete', 45)
        self.cooper = Participant('Cooper', 45)

        self.comp.addParticipant(self.roger)
        self.comp.addParticipant(self.jane)
        self.comp.addParticipant(self.pete)
        self.comp.addParticipant(self.cooper)
        
        self.comp.distributePrizes()

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
        # self.skipTest("Parts III & IV")

        self.peggy = Participant('Peggy', 77)
        self.tom = Participant('Tom', 66)
        self.joan = Participant('Joan', 66)
        self.ken = Participant('Ken', 45)

        self.comp.addParticipant(self.peggy)
        self.comp.addParticipant(self.tom)
        self.comp.addParticipant(self.joan)
        self.comp.addParticipant(self.ken)

        self.comp.distributePrizes()

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
        # self.skipTest("Example four")
        
        self.harry = Participant('Harry', 77)
        self.lane = Participant('Lane', 45)
        self.stan = Participant('Stan', 45)
        self.henry = Participant('Henry', 45)

        self.comp.addParticipant(self.harry)
        self.comp.addParticipant(self.lane)
        self.comp.addParticipant(self.stan)
        self.comp.addParticipant(self.henry)

        self.comp.distributePrizes()

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
        # self.skipTest("Example five")

        self.ted = Participant('Ted', 77)
        self.trudy = Participant('Trudy', 77)
        self.bobby = Participant('Bobby', 46)
        self.paul = Participant('Paul', 46)

        self.comp.addParticipant(self.ted)
        self.comp.addParticipant(self.trudy)
        self.comp.addParticipant(self.bobby)
        self.comp.addParticipant(self.paul)

        self.comp.distributePrizes()

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

if __name__ == "__main__":
    main()
