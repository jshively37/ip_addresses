# IP Address Reputation Validation

Python script to validate the reputation of IP addresses.

## Requirements

The script relies on an API service from [ipdata.co](ipdata.co), so you will need to register for and obtain an IP key.

## The script

The `validate_ip.py` file has the skeleton of the script that needs to be developed.

```python
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

```

### :keyboard: Activity: Fork this repository

Fork this repository to your Github account. This will give you the proper read and write access to make all of the changes required to complete the exercise.

### :keyboard: Activity: Clone your forked repository

Clone the repository down to your local development workstation.

```sh
git clone https://github.com/<YOUR USERNAME>/ip_addresses.git
```

### :keyboard:Activity: Read and update the scripts documentation

The documentation for the script includes information about features to provided by the script. It also includes steps that you should follow in order to obtain the API key to use the service that the script will use to validate the IP addresses. Finally, read through the inline comments to complete the functionality listed in each of the sections.

### :keyboard:Activity: Develop your script

Once you have completed your script, be sure to test it with the sample text file `addresses.txt` included in this repository. You can do so by running your script as follows:

```sh
python validate.py addresses.txt
```

### :keyboard:Activity: Commit and push your changes

Once you have validated that your script functions as expected, commit the changes to history using `Git` and push them up to your upstream repository.

### :keyboard:Activity: Submit a Merge Request to this repository

From Github, submit a Merge request from your repository back to this one.