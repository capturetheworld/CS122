def most_words(*args):
    """
    Returns the string with the most number of words
    :param any number of strings: (*args)
    :return: the string with the most number of words (string)
    """

    #
    # wordiest_phrase= None
    # word_count = 0
    # for arg in args:f
    #     temp_counter = (lambda x: len(x.split()))(arg) #wordcounter
    #     if (word_count< temp_counter):
    #         word_count = len(arg.split())
    #         wordiest_phrase = arg

    return max(args, key=lambda phrase: len(phrase.split()), default=
    None)

    # return wordiest_phrase