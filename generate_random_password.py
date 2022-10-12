#!/usr/bin/env python3
"""
Generate a random password in the style of the Apple iCloud Keychain.

"xxxxxx-xxxxxx-xxxxxx"

where x: random uppercase and lowercase characters or digits

Usage:
    $ python /path/to/script.py


"""

import sys
import math
import random
import string
import argparse

def cmdline_args():
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("-l", "--length", type=int_range(5,25), default=6, help="length of individual phrases")
    p.add_argument("-n", "--number", type=int_range(1,3), default=3, help="number of phrases")
    p.add_argument("-s", "--sep", type=str, default='-', help="separator")
    p.add_argument("-a", "--exclude_ambiguous", type=bool, default=True, help="exclude the ambiguous characters iIlL1oO0")

    return(p.parse_args())


def int_range(mini,maxi):
    """Return function handle of an argument type function for 
       ArgumentParser checking a float range: mini <= arg <= maxi
         mini - minimum acceptable argument
         maxi - maximum acceptable argument"""

    # Define the function with default arguments
    def int_range_checker(arg):
        """New Type function for argparse - a float within predefined range."""
        try:
            f = int(arg)
        except ValueError:    
            raise argparse.ArgumentTypeError("must be an integer number")
        if f < mini or f > maxi:
            raise argparse.ArgumentTypeError("must be in range [" + str(mini) + " .. " + str(maxi)+"]")
        return f

    # Return function handle to checking function
    return int_range_checker

if __name__ == '__main__':
    
    if sys.version_info<(3,6,0):
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit(1)

    args = cmdline_args()

    # calculate length of the password excluding sep characters
    password_length = args.length * args.number

    # possible characters to use for the password
    population = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    # drop ambigious characters if user requested
    if args.exclude_ambiguous:
        for char in "iIlL1oO0":
            population.remove(char)

    # sample characters with replacement
    sampled_chars = random.choices(population, k=password_length)

    # group characters into phrases 
    phrases = []
    for i in range(args.number):
        m = i * args.length
        n = (i + 1) * args.length
        phrase = ''.join(sampled_chars[m:n])
        phrases.append(phrase)

    # join phrases using the sep character
    password = args.sep.join(phrases)

    print(password)
