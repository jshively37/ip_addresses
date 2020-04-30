#! /usr/bin/env python
"""
Author: { your name here }

This script is a utility to validate the reputation of IP addresses.

It uses the ipdata.co reputation services to check if supplied IP address.
You need register for an API key from ipdata.co

The script accepts a command line argument for the name of the file that
contains the IP addresses to verified. It uses the `sys` module from the
standard library to parse the argument.

The script also relies on the third party `requests` library to consume the
API service from ipdata.co


example usage:
    $ python validate_ip.py addresses.txt

"""
import sys

import requests


API_KEY = ''  # insert your api key here for ipdata.co


def main(arguments):
    """
    Main entry point for the script
    """

    # The cli arguments passed in is in the form of list. Uncomment the
    # line below to see the arguments printed.
    # print(arguments)

    # assign the argument for the filename to a variable named `filename`
    filename = ''

    # open the file using a context manager. this will ensure that the file
    # is automatically closed once you're done. assign the contents of the
    # file to a variable named `file_content`

    # loop through each IP in the file and use the request library to make
    # a GET call to the ipdata.co service.
    # example for each call: f'https://api.ipdata.co/{ip}?api-key={API_KEY}'

    # print out the list of IPs that are categorized as threats. As a bonus,
    # save the output out as a csv file. hint: Python has a `csv` module
    # in the standard library.


if __name__ == '__main__':
    cli_arguments = sys.argv    # using sys to parse the CLI arguments
    main(cli_arguments)         # call our main function w arguments
