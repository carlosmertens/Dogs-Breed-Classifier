"""Program to format time in hh:mm:ss and print it."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# */Courses-Projects/Udacity/My_AIPND_Project1/format_timer.py
#
# PROGRAMMER: Carlos Mertens
# DATE CREATED: 10/05/2018
# REVISED DATE: (MM/DD/YY) - Not revise it yet
# PURPOSE: To format test timing to format hh:mm:ss
#
# To be called as method time_formatted() from other scripts or call directly
#   Example call:
#    python format_timer.py
##

# Import
from time import time, sleep


# Main program function
def main():
    """Start, sleep and end code to test running time."""
    start_time = time()
    sleep(1)
    end_time = time()
    print("\n** Total Elapsed Runtime in seconds:", end_time - start_time)

    # Call function to format time tested
    time_formatted(end_time, start_time)


# Function to format time to hh:mm:ss
def time_formatted(end_time, start_time):
    """Format time in hh:mm:ss and print it."""
    # Calculate time rounding to the nearest second
    total_time = round(end_time - start_time)

    # Calculate hours (3600 second in an hour)
    hh = str(total_time // 3600)
    if len(hh) < 2:
        hh = "0" + hh

    # Calculate minutes (60 seconds in a minute)
    mm = str((total_time % 3600) // 60)
    if len(mm) < 2:
        mm = "0" + mm

    # Calculate seconds
    ss = str((total_time % 3600) % 60)
    if len(ss) < 2:
        ss = "0" + ss

    print("\n** Runtime formated to hh:mm:ss: {}:{}:{}\n".format(hh, mm, ss))


if __name__ == "__main__":
    main()
