# -*- encoding: utf-8 -*-

"""

About : Anagram Matching Code.

"""

__author__ = "Eduard Florea"
__email__ = "viper6277@gmail.com"
__copyright__ = "Copyright (C) 2020 {a}".format(a=__author__)
__credits__ = ""
__license__ = "MIT"
__version__ = 0.01
__lastdate__ = "2020-05-04"

# ----------------------------------------------------------------------------------------------------------------------
#
# Supporting libraries
#

import time

# ----------------------------------------------------------------------------------------------------------------------
#
# Support Functions
#

def word_dict(filename: str) -> dict:

    wdict = {}

    # Uncomment for testing only
    start_time = time.time()

    wc = 0

    with open(filename, 'r') as fh:

        for line in fh.readlines():

            word = line.strip()
            word = word.lower()

            wdict[word] = {'Count': len(word), 'Char List': [x for x in word]}

            wc += 1

    # Uncomment for testing only
    time_elapsed = time.time() - start_time
    print("\n\tParsed {n} word dictionary in : {t:.15f} seconds".format(
        n=wc,
        t=time_elapsed))

    return wdict


def let_count(word: str) -> dict:
    """
    Returns the count of letters in a string as a dictionary
    """

    return {x: word.count(x) for x in set([x for x in word])}


# ----------------------------------------------------------------------------------------------------------------------


def main():

    # Master Word Dictionary
    m_word_dict = word_dict('words_small.txt')

    def is_anagram(word: str) -> bool:

        word_len = len(word)

        word_char_list = [x for x in word]

        word_let_count = let_count(word)

        accepted_words = []

        candidate_list = []
        for k, v in m_word_dict.items():
            if word_len == v['Count']:
                candidate_list.append(k)

        #print(len(candidate_list))

        # --------------------------------------------------------------------------------------------------------------

        for x in candidate_list:

            word_details = m_word_dict[x]

            candidate_char_list = word_details['Char List']

            # full letter match
            flm = False
            i = 0
            for y in candidate_char_list:

                if y not in word_char_list:
                    break

                else:

                    # Candidate, letter count...
                    clc = candidate_char_list.count(y)

                    #
                    # Here we are matching letter counts, so the wrong letter is not duplicated.
                    #
                    if clc != word_let_count[y]:
                        break

                    else:
                        i += 1

            if i == word_len:
                flm = True

            # ----------------------------------------------------------------------------------------------------------
            #
            # Duplicate letter checking
            #

            if flm is True:
                accepted_words.append(x)

        # --------------------------------------------------------------------------------------------------------------

        # Uncomment for testing
        print(accepted_words)

        if accepted_words:
            return True
        else:
            return False

    # ------------------------------------------------------------------------------------------------------------------

    # "abidance" or..... "dceaniba"

    # Uncomment for testing only
    start_time = time.time()

    is_anagram('dceaniba')

    # Uncomment for testing only
    time_elapsed = time.time() - start_time
    print("\n\tExecuted in : {t:.15f} seconds".format(t=time_elapsed))


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
