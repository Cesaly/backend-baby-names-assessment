#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = "Cesaly with help from demo"

import sys
import re
import argparse


def extract_names(filename):
    names = []
    with open(filename) as f:
        text = f.read()

    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:

        sys.stderr.write('Couldn\'t find the year!\n')
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><\td>(\w+)<\td>')

    names_to_rank = {}
    for rank_tuple in tuples:
        (rank, boyname, girlname) = rank_tuple
    if boyname not in names_to_rank:
        names_to_rank[boyname] = rank
    if girlname not in names_to_rank:
        names_to_rank[girlname] = rank

    sorted_names = sorted(names_to_rank.keys())

    for name in sorted_names:
        names.append(name + " " + names_to_rank[name])

    return names


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser(description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command-line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command-line arguments into a NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names` with that single file.
    # Format the resulting list a vertical list (separated by newline \n)
    # Use the create_summary flag to decide whether to print the list,
    # or to write the list to a summary file e.g. `baby1990.html.summary`

    # +++your code here+++


if __name__ == '__main__':
    main(sys.argv[1:])
