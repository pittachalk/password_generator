#!/usr/bin/env python3
"""
Generate a random password in the style of the Apple iCloud Keychain.

"xxxxxx-xxxxxx-xxxxxx"

where x: random uppercase and lowercase characters or digits

Usage:
    $ python /path/to/script.py


"""

import sys
import random
import string
import argparse

def cmdline_args():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("-l", "--length", type=int, default=6, help="length of individual phrases")
    p.add_argument("-n", "--number", type=int, default=3, help="number of phrases")
    p.add_argument("-s", "--sep", type=str, default='-', help="separator")
    p.add_argument("-a", "--exclude_ambiguous", type=bool, default=True, help="exclude the ambiguous characters lL1oO0")

    return(p.parse_args())


if __name__ == '__main__':
    
    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)

    args = cmdline_args()

    # possible characters to use for the password
    population = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    if args.exclude_ambiguous:
        for char in "ilL1oO0":
            population.remove(char)

    phrases = []
    for i in range(args.number):
        sampled_chars = random.sample(population, args.length)
        phrase = ''.join(sampled_chars)
        phrases.append(phrase)

    password = args.sep.join(phrases)
    print(password)
