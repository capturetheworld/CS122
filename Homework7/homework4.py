# ----------------------------------------------------------------------
# Name:    Homework 4
# Purpose: Practice set problems
#
# Author:  Ian Soohoo and Trieu Nguyen
# ----------------------------------------------------------------------
"""Homework 4

Set Problems
"""


def hottest(cities, n=4):
    """Hottest n cities

    The function returns a list that contains the names of
    the hottest n cities.  The list is sorted with
    the hottest city first. The function does not modify
    the original dictionary.

    :param city: a dictionary of arbitrary size representing cities
    :param temp: an integer
    :return: a list that contains the names of the hottest n cities
    """

    return list(sorted(cities, key=cities.get, reverse=True))[:n]


def common_words(string1, string2):
    """Number of common unique words

    The function returns the number of  unique words that are common
     to both strings - regardless of case.

    :param string1: first string
    :param string2: second string
    :return: integer result number of unique words
    """
    words_string1 = string1.lower().split()
    words_string2 = string2.lower().split()

    set1 = set()
    set2 = set()

    for each_word in words_string1:
        set1.add(each_word)

    for each_word in words_string2:
        set2.add(each_word)

    return len(set(set1).intersection(set2))


def alert(grades):
    """Find students who have at least one grade below 50

    Takes as parameter a dictionary of arbitrary size
    representing student grades. The dictionary keys are
    students' names and the values are lists of their grades.

    :param : dictionary of arbitrary size
    :return: a set that contains the names of the students
    who have grade below 50
    """

    return {grade for grade in grades
            if any(u < 50 for u in grades[grade])}


def make_password(input_string):
    """Create a password from an input string

       Takes as parameter a string that the user inputs a string. Strips
       spaces so that only the characters remain. Grabs the first
       character of each word and uses concats them together then
       returns the new string in all uppercase

       :param : a string with or without spaces to make a password from
       :return: the new password string
       """

    return (''.join(word[0] for word in input_string.split(
    )).upper())

def extra_credit(grades,points=1):
    """Add extra credit to grades

       Takes a dictionary parameter of key value student-grade pairs
       adds points to each grade, if none specified add 1 extra credit
       point

       :param : dictionary of arbitrary size, integer for points
       :return:  modified dictionary
       """
    for grade in grades:
        grades[grade] = grades[grade]+points

    return grades




def main():
    print("Test hottest function: ")

    no_cities = {}
    norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70, 'Sacramento': 75,
              'San Francisco': 64, 'San Jose': 73, 'Oakland': 67,
              'Los Altos': 71, 'Mountain View': 72}
    print(hottest(norcal, 2))
    # ['Fresno', 'Sacramento']
    print(hottest(norcal))
    # ['Fresno', 'Sacramento', 'Napa', 'San Jose']
    print(hottest(norcal, 8))
    # ['Fresno', 'Sacramento', 'Napa', 'San Jose', 'Mountain View',
    # 'Los Altos', 'Palo Alto', 'Oakland']
    print(hottest(norcal, 20))
    # ['Fresno', 'Sacramento', 'Napa', 'San Jose', 'Mountain View',
    # 'Los Altos', 'Palo Alto', 'Oakland', 'San Francisco']
    print(norcal)
    # {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70, 'Sacramento': 75,
    # 'San Francisco': 64, 'San Jose': 73, 'Oakland': 67,
    # 'Los Altos': 71, 'Mountain View': 72}

    print(hottest(no_cities, 6))  # []

    print()
    print("Test common_words")
    phrase1 = '''Simple is better than     complex and flat
                is better than nested'''
    phrase2 = '''Complex is  better than complicated
                and  Sparse is better than dense'''
    print(common_words(phrase1, phrase2))  # should print 5

    print(common_words('', ''))  # should print 0
    print(common_words('Hi Class', 'Hello world'))  # should print 0

    print()
    print("Test alert")
    disney_class = {'Mickey': [78, 50, 100], 'Minnie': [88, 65, 99, 70],
                    'Pluto': [70, 49, 87, 66, 38], 'Donald': [40]}
    cs122 = {'Alex': [76, 90], 'Diana': [100, 100, 100],
             'Zoe': [50, 87, 90, 100]}
    empty_class = {}

    print(alert(disney_class))  # {'Donald', 'Pluto'}
    print(disney_class)  # unchanged
    print(alert(cs122))  # empty set
    print(cs122)  # unchanged
    print(alert(empty_class))  # empty set
    print(empty_class)  # unchanged

    print(make_password( 'Simple is       better than \t complicated'))
    print(make_password('python'))
    print(make_password(''))

    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}
    print(extra_credit(cs122))  # {'Zoe':91, 'Alex': 94, 'Dan':80,
    # 'Anna':101}
    print(cs122)  # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(extra_credit(cs122, 2))  # {'Zoe':93, 'Alex': 96, 'Dan':82,
    # 'Anna':103}
    print(cs122)  # {'Zoe':93, 'Alex': 96, 'Dan':82, 'Anna':103}
    print(extra_credit(empty_class, 5))  # {}

if __name__ == "__main__":
    main()