# ----------------------------------------------------------------------
# Name:    Homework 5
# Purpose: Practice set problems
#
# Author:  Ian SooHoo
# ----------------------------------------------------------------------
import string


def word_lengths(phrase):
    """
      Counts the lengths of words in a phrase
      :param phrase: (string)
      :return: a dictionary with the words and lengths of words as key
      value pairs
      """
    return {word.strip(string.punctuation): len(word) for word in
            phrase.lower().split()}


def geometric_sum(limit):
    """
     Finds the geometric sum to a limit
     :param limit: (integer)
     :return: the sum of the geometric sequence
     """
    total = sum(1 / (2 ** x) for x in range(1, limit + 1))  # generator
    return total


def most_words(*args):
    """
    Returns the string with the most number of words
    :param any number of strings: (*args)
    :return: the string with the most number of words (string)
    """

    #
    # wordiest_phrase= None
    # word_count = 0
    # for arg in args:
    #     temp_counter = (lambda x: len(x.split()))(arg) #wordcounter
    #     if (word_count< temp_counter):
    #         word_count = len(arg.split())
    #         wordiest_phrase = arg

    return max(args, key=lambda phrase: len(phrase.split()), default=
    None)

    # return wordiest_phrase


def coolest(cities, number=3):
    """
    Returns the cities with the coolest average temperatrues
    :param cities: and temps (dictionary)
    :param number: default is 3 (int) how many cities starting with
    coolest
    :return: cities that are the coolest (list)
    """
    # return [cities,key = lambda city: statistics.mean(cities[city])]
    return sorted(cities, key=lambda city: sum(cities[city]) / len(
        cities[city]), )[0:number]


def secret(function):
    """
        A decorator that modifies strings
        :param sentence: Any number of parameters, first must
        be a string
        :return: the rearranged values (string)
        """
    # print("RIGHT HERE2")
    def wrapper(*sentence):
        # print("RIGHT HERE3")
        if len(sentence) is 1:
            words = function(sentence[0]).split()
        else:
            words = function(sentence[0], sentence[1]).split()
        words = [word.upper() for word in words]
        # print(words)
        #
        # for word in words:
        #     if (word[0] is ('A' or 'E' or 'I' or 'O' or 'U')):
        #         print("YEP")
        #         print(word[0])
        # for word in words:
        #     if ('B' == 'A' or 'E'):
        #         print("YES")
        #         print(word[0])

        words = [word + "PIN" if word[0] is 'A' or word[0] is 'E' or
                                 word[0] is 'I' or word[0] is 'O' or
                                 word[0] is 'U'
                 else word[1:] + word[0] + "IP" for word in words]
        # for word in words:
        #     print(word[0])
        # print(words)
        # print("HERE WE GO")

        # for word in words:
        #
        #     if (word[0] is 'A' or 'E' or 'I' or 'O' or 'U'):
        #         print("RIGHT HERE9")
        #         words[word] = word+"PIN"
        #     else:
        #         word[word] = word[1:]+"IP"

        words = " ".join(words)
        len(sentence)
        if len(sentence) > 1:
            return words, ""
        else:
            return words

    return wrapper


@secret
def greet(name):
    """
    Return a personalized hello message.
    :param name: (string)
    :return: (string)
    """

    return f'Hello {name}'


@secret
def repeat(phrase, n):
    """
    Repeat the specified string n times
    with a space character in between.
    :param phrase: (string)
    :param n: number of times the phrase will be repeated
    :return:
    """
    words = phrase.split()
    return ' '.join(n * words)


def main():
    phrase = '''Simple is better than     complex, and flat
                 IS BETTER than nested!?!'''
    print(word_lengths(''))
    print(word_lengths(phrase))
    print(geometric_sum(-5))  # 0
    print(geometric_sum(0))  # 0
    print(geometric_sum(1))  # 0.5
    print(geometric_sum(2))  # 0.75
    print(geometric_sum(3))  # 0.875
    print(geometric_sum(4))  # 0.9375
    print(geometric_sum(30))  # 0.9999999990686774

    print(most_words())

    print(most_words('pneumonoultramicroscopicsilicovolcanoconiosis',

                     'Go Spartans!', 'Are you     ready?'))

    norcal = {'Fresno': [77, 68, 80], 'Napa': [74, 89, 92, 55],
              'Palo Alto': [70, 78, 62], 'Sacramento': [75, 91, 92, 89],
              'San Francisco': [64, 59, 78], 'San Jose': [73, 85, 89],
              'Oakland': [67, 68, 61], 'Los Altos': [91, 58],
              'Mountain View': [72, 85, 90]}

    no_cities = {}

    print(coolest(no_cities, 100))  # []
    print(coolest(norcal))  # ['Oakland', 'San Francisco', 'Palo Alto']
    print(coolest(norcal,
                  5))  # ['Oakland', 'San Francisco', 'Palo Alto', 'Los Altos', 'Fresno']
    print(coolest(norcal,
                  10))  # ['Oakland', 'San Francisco', 'Palo Alto', 'Los Altos', 'Fresno', 'Napa', 'San Jose', 'Mountain View', 'Sacramento']
    print(norcal)  # unchanged
    print(no_cities)  # {}
    print(greet('Universe'))  # ELLOHIP UNIVERSEPIN
    print(repeat('Explicit is better than implicit',
                 2))  # EXPLICITPIN ISPIN ETTERBIP HANTIP IMPLICITPIN EXPLICITPIN ISPIN ETTERBIP HANTIP IMPLICITPIN


if __name__ == "__main__":
    main()
