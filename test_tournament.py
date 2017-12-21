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
        #self.skipTest("Part II")

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
        self.skipTest("Parts III & IV")

        self.prizes = {
            1: 50,
            2: 20,
            3: 10,
        }

    def test_example_one(self):
        pass

    def test_example_two(self):
        pass

    def test_example_three(self):
        pass

    def test_example_four(self):
        pass

    def test_example_five(self):
        pass
