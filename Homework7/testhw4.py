import unittest
import homework4 as hw4
# ----------------------------------------------------------------------
# Name:    Homework 7
# Purpose: Unit Test cases
#
# Author:  Ian SooHoo
# ----------------------------------------------------------------------


class TestQ1(unittest.TestCase):
    """
    Tests the hottest function method
    """

    def setUp(self):
        """Create a few dictionaries"""
        self.no_cities = {}
        self.norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70,
                       'Sacramento': 75, 'San Francisco': 64, 'San Jose': 73,
                       'Oakland': 67, 'Los Altos': 71, 'Mountain View': 72}

    def test_hottest_few(self):
        """Tests to find a few cities"""
        self.assertEqual(hw4.hottest(self.norcal, 2), ['Fresno',
                                                       'Sacramento'])

    def test_hottest_default(self):
        """Tests to find hottest cities defaults to 4"""
        self.assertEqual(hw4.hottest(self.norcal), ['Fresno', 'Sacramento',
                                                    'Napa', 'San Jose'])

    def test_hottest_more(self):
        """Tests to find 8 hottest cities"""
        self.assertEqual(hw4.hottest(self.norcal, 8), ['Fresno', 'Sacramento',
                                                       'Napa', 'San Jose',
                                                       'Mountain View',
                                                       'Los Altos',
                                                       'Palo Alto', 'Oakland'])

    def test_hottest_twenty(self):
        """Tests to see printing of 20 hottest"""
        self.assertEqual(hw4.hottest(self.norcal, 20), ['Fresno', 'Sacramento',
                                                        'Napa', 'San Jose',
                                                        'Mountain View',
                                                        'Los Altos',
                                                        'Palo Alto',
                                                        'Oakland',
                                                        'San Francisco'])

    def test_dictionary(self):
        """Tests the setup dictionary"""
        self.assertEqual(self.norcal, {'Fresno': 77, 'Napa': 74,
                                       'Palo Alto': 70, 'Sacramento': 75,
                                       'San Francisco': 64,
                                       'San Jose': 73, 'Oakland': 67,
                                       'Los Altos': 71,
                                       'Mountain View': 72})
    def test_hottest_no_modify(self):
        """Tests the to see if hottest the dictionary"""
        self.assertEqual(hw4.hottest(self.norcal, 8), ['Fresno', 'Sacramento',
                                                       'Napa', 'San Jose',
                                                       'Mountain View',
                                                       'Los Altos',
                                                       'Palo Alto', 'Oakland'])
        self.assertEqual(self.norcal, {'Fresno': 77, 'Napa': 74,
                                       'Palo Alto': 70, 'Sacramento': 75,
                                       'San Francisco': 64,
                                       'San Jose': 73, 'Oakland': 67,
                                       'Los Altos': 71,
                                       'Mountain View': 72})

    def test_hottest_nocities(self):
        """Tests hottest with an empty dictionary"""
        self.assertEqual(hw4.hottest(self.no_cities, 6), [])


class TestQ2(unittest.TestCase):
    """
    Tests the common_words function
    """

    def setUp(self):
        """phrases"""
        self.phrase1 = '''Simple is better than     complex and flat 
             is better than nested'''
        self.phrase2 = '''Complex is  better than complicated 
             and  Sparse is better than dense'''

    def test_common_words_phrases(self):
        """Tests common words via pre"""
        self.assertEqual(hw4.common_words(self.phrase1, self.phrase2), 5)

    def test_common_words_empty(self):
        """Tests common words via direct entry and empty strings"""
        self.assertEqual(hw4.common_words("", ""), 0)

    def test_common_words_empty_spaces(self):
        """Tests common words via direct entry and a bunch of spaces"""
        self.assertEqual(hw4.common_words("          ", "    "), 0)

    def test_common_words_direct_entry(self):
        """Tests common words via direct entry"""
        self.assertEqual(hw4.common_words('Hi Class', 'Hello world'), 0)

    def test_common_words_numbers(self):
        """Tests common words via numbers"""
        self.assertEqual(hw4.common_words('Hi 2 Class', 'Hello 2 Class'), 2)


class TestQ3(unittest.TestCase):
    """
    Tests the alert function
    """

    def setUp(self):
        """dictionaries"""
        self.disney_class = {'Mickey': [78, 50, 100], 'Minnie': [88, 65, 99,
                                                                 70],
                             'Pluto': [70, 49, 87, 66, 38], 'Donald': [40]}
        self.cs122 = {'Alex': [76, 90], 'Diana': [100, 100, 100],
                      'Zoe': [50, 87, 90, 100]}
        self.empty_class = {}

    def test_alert_low_grades(self):
        """Tests the alert function for low grades"""
        self.assertEqual(hw4.alert(self.disney_class), {'Donald', 'Pluto'})

    def test_alert_unchanged(self):
        """Tests the alert function to make sure it doesn't modify
        dictionary"""
        self.assertEqual(hw4.alert(self.disney_class), {'Donald', 'Pluto'})
        self.assertEqual(self.disney_class, {'Mickey': [78, 50, 100],
                                             'Minnie': [88, 65, 99, 70],
                                             'Pluto': [70, 49, 87, 66, 38],
                                             'Donald': [40]})

    def test_alert_no_issues(self):
        """Tests the alert function with a set that's okay"""
        self.assertEqual(hw4.alert(self.cs122), set())

    def test_alert_empty_set(self):
        """Tests the alert function with an empty set"""
        self.assertEqual(hw4.alert(self.empty_class), set())

    def test_alert_empty_unchanged(self):
        """Tests the alert function with an empty set and then
        checks to see the original empty wasn't modified"""
        self.assertEqual(hw4.alert(self.empty_class), set())
        self.assertEqual(self.empty_class, {})

    def test_alert_122(self):
        """Checks to see if running a class with no low grades, but has
        elements through the alert class will modify the original"""
        self.assertEqual(hw4.alert(self.cs122), set())
        self.assertEqual(self.cs122, {'Alex': [76, 90], 'Diana':
            [100, 100, 100], 'Zoe': [50, 87, 90, 100]})


class TestQ4(unittest.TestCase):
    """
    Tests password function
    """

    def test_make_password(self):
        """Tests make password with a sentence"""
        self.assertEqual(hw4.make_password('Simple is       better than  \t '
                                           'complicated'), 'SIBTC')

    def test_make_password_single_word(self):
        """Tests make password with a word"""
        self.assertEqual(hw4.make_password('python'), 'P')

    def test_make_password_blank(self):
        """Tests make password with blank"""
        self.assertEqual(hw4.make_password(''), '')

    def test_make_password_spaces(self):
        """Tests make password with spaces"""
        self.assertEqual(hw4.make_password('              '), '')

    def test_make_password_tabs(self):
        """Tests make password with tabs to see if they are stripped"""
        self.assertEqual(hw4.make_password('              '), '')


class TestQ5(unittest.TestCase):
    """
    Tests extra credit function
    """

    def setUp(self):
        """sets up dictionaries"""
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_extra_credit_output_default(self):
        """Tests adding extra credit default"""
        self.assertEqual(hw4.extra_credit(self.cs122), {'Zoe': 91, 'Alex': 94,
                                                        'Dan': 80,
                                                        'Anna': 101})

    def test_extra_credit_output(self):
        """Tests adding extra credit with a parameter passed"""
        self.assertEqual(hw4.extra_credit(self.cs122, 2), {'Zoe': 92,
                                                           'Alex': 95,
                                                           'Dan': 81,
                                                           'Anna': 102})

    def test_extra_credit_does_modify(self):
        """Check to see if the function IS modifying the argument"""
        self.assertEqual(hw4.extra_credit(self.cs122), {'Zoe': 91, 'Alex': 94,
                                                        'Dan': 80,
                                                        'Anna': 101})
        self.assertEqual(self.cs122, {'Zoe': 91, 'Alex':
            94, 'Dan': 80, 'Anna': 101})

    def test_extra_credit_continuous(self):
        """Check to see if continuing calling method will cause it ot
        break"""
        self.assertEqual(hw4.extra_credit(self.cs122), {'Zoe': 91, 'Alex': 94,
                                                        'Dan': 80,
                                                        'Anna': 101})
        self.assertEqual(hw4.extra_credit(self.cs122, 2), {'Zoe': 93, 'Alex':
            96, 'Dan': 82, 'Anna': 103})

    def test_extra_credit_empty(self):
        """Test to see extra credit handling empty dictionary"""
        self.assertEqual(hw4.extra_credit(self.empty_class), {})
