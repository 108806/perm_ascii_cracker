#! /usr/bin/env python3
#   coding=utf-8

import os
import re
import time
import unittest

__author__ = "__T4K32H1__"

# GET WORKING DIR:
print(f'''CURRENT WORKING DIR IS :\n{os.getcwd()}\n''')
# INIT THE FILES:
coded, words = open("scrambled-words.txt", "r", encoding="UTF-8"), open("dictionary.txt", encoding="UTF-8")
coded, words = [x.strip('\n') for x in coded], [x.strip('\n') for x in words]
# VERBOSE:
print(F"""Length of coded file is : {len(coded)}, length of words file is : {len(words)}\n""")


# V.COOL PERFORMANCE MEASURING FUNCTION FROM STACK OVERFLOW:
def timerfunc(func):
    """
    A timer decorator
    """

    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value

    return function_timer


# SIMPLE GET K FUNCTION:
def get_keys(dict, value):
    return [k for k in dict.keys() if (dict[k] == value)]


# CHECKING TWO STRINGS FOR BEING PERMUTATIONS:
def chars_check(str1, *str2):
    for _string in str2:
        _s = _string
        if len(str1) != len(_string):
            return False
        for x in range(len(_string)):
            if str1[x] not in list(_string):
                return False
            else:
                _string = _string.replace(str1[x], '*', 1)
        return str1, _s


# TEST THE SPEAR OF ODIN:
class chars_test(unittest.TestCase):
    def test(self):
        self.assertTrue(chars_check("zupa", "apuz"))
        self.assertFalse(chars_check("zupa", "zupaa"))
        self.assertFalse(chars_check("zupp", "zupa"))
        self.assertFalse(chars_check("zupp", ["zupa", "zpa", "zzzzz"]))


# EXECUTE THE TEST for debug:
if __name__ == '__main__':
    unittest.main(exit=False)


# GET LOW AND COMPARE:
@timerfunc
def bit_ops(coded, words, matches=[], cnt=0):
    print("\nPreparing the dictrionaries...\n")
    ascii_sums_words = {word: sum([ord(char) for char in word]) for word in words}
    ascii_sums_cwords = {word: sum([ord(char) for char in word]) for word in coded}
    print(F"""Words dict length: {len(ascii_sums_words)}\nCoded words dict length: {len(ascii_sums_cwords)}\n""")
    print("\nDone.\nSearching for matches, this can take a while...\n")

    # NOTE - THIS CAN MAKE A BUG OF INSERTING RANDOM DUPS IF USED NOT WITH A DICT:
    for x in ascii_sums_cwords.values():
        hits = [get_keys(ascii_sums_words, x)]

        for hit in hits:
            for _word in hit:
                cnt += 1
                print(f'\rWords with the same ascii value: {cnt}', sep='\t', end='\t', flush=False)
                pair = chars_check(_word, *get_keys(ascii_sums_cwords, x))
                if pair not in matches:
                    matches.append(pair)
                print(pair, sep='\t', end='\t')


    # NOW JUST SHOW IT NICELY...
    final = [re.sub(r"[(\()?(\))?(\')?(\,)?]", '', ':'.join(str(match).split())) for match in
             filter(lambda m: m != False, matches)]
    
    # OPTIONAL : PRINT THE MATCHES:
    print('\nMatched words are: ', *final, sep='\n')

    # AND WRITE IT ALL TO THE FILE:
    with open('matches.txt', 'w+', encoding='UTF-8') as f:
        f.writelines(w + '\n' for w in final)
        f.close()

    print("\nAll done. Results were saved in file matches.txt.\nQuitting now...")


# EXECUTE:
bit_ops(coded, words)

# DO IT BETTER: STREAM ALL DATA AT CHARS_TEST WITH RECU
