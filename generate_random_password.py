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
    p.add_argument("-u", "--uppercase_prop", type=float_range(0,1), default=0.1, help="proportion of upper case characters")
    p.add_argument("-d", "--digit_prop", type=float_range(0,1), default=0.1, help="proportion of digits")
    
    # https://stackoverflow.com/questions/44561722/why-in-argparse-a-true-is-always-true
    p.add_argument('--exclude_ambiguous', default='', action='store_false', help='exclude the ambiguous characters iIlL1oO0')

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

def float_range(mini,maxi):
    """Return function handle of an argument type function for 
       ArgumentParser checking a float range: mini <= arg <= maxi
         mini - minimum acceptable argument
         maxi - maximum acceptable argument"""

    # Define the function with default arguments
    def float_range_checker(arg):
        """New Type function for argparse - a float within predefined range."""
        try:
            f = float(arg)
        except ValueError:    
            raise argparse.ArgumentTypeError("must be a float number")
        if f < mini or f > maxi:
            raise argparse.ArgumentTypeError("must be in range [" + str(mini) + " .. " + str(maxi)+"]")
        return f

    # Return function handle to checking function
    return float_range_checker

if __name__ == '__main__':
    
    if sys.version_info<(3,6,0):
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit(1)

    args = cmdline_args()

    # check that the uppercase and digit proportions to not sum up to above 1
    if (args.uppercase_prop + args.digit_prop) > 1:
        raise ValueError("Digit and upper case proportions cannot exceed 1 in total!")

    # calculate length of the password excluding sep characters
    password_length = args.length * args.number

    # number of characters of each type
    num_uppercase = math.ceil(password_length * args.uppercase_prop)
    num_digit = math.ceil(password_length * args.digit_prop)
    num_lowercase = password_length - num_uppercase - num_digit

    # possible characters to use for the password
    # population = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    population_lowercase = list(string.ascii_lowercase)
    population_uppercase = list(string.ascii_uppercase)
    population_digit = list(string.digits)

    # drop ambiguous characters if user requested
    # based on https://stackoverflow.com/questions/4915920/how-to-delete-an-item-in-a-list-if-it-exists
    if args.exclude_ambiguous == False:
        for char in "iIlL1oO0":
            try:
                population_lowercase.remove(char)
            except ValueError:
                try:
                    population_uppercase.remove(char)
                except ValueError:
                    try:
                        population_digit.remove(char)
                    except ValueError:
                        pass

    # sample characters with replacement
    sampled_lowercase = random.choices(population_lowercase, k=num_lowercase)
    sampled_uppercase = random.choices(population_uppercase, k=num_uppercase)
    sampled_digit = random.choices(population_digit, k=num_digit)

    # join these lists, then shuffle the order
    sampled_chars = sampled_lowercase + sampled_uppercase + sampled_digit
    sampled_chars = random.sample(sampled_chars, len(sampled_chars))

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
