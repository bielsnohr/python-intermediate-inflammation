"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array.

    :param data: 2d inflammation data array. 0th axis (rows) are patients
    indexes, and 1st axis (columns) are the day index.
    :returns: 1d array with the daily mean for all patients' inflammation values
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array.

    :param data: 2d inflammation data array. 0th axis (rows) are patients
    indexes, and 1st axis (columns) are the day index.
    :returns: 1d array with the daily maximum for all patients' inflammation
    values
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array.

    :param data: 2d inflammation data array. 0th axis (rows) are patients
    indexes, and 1st axis (columns) are the day index.
    :returns: 1d array with the daily minimum for all patients' inflammation
    values
    """
    return np.min(data, axis=0)


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
