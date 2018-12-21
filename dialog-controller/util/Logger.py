#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Accenture"
__copyright__ = "Copyright 2018, Accenture"

import logging

logging.basicConfig()
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)


def log(message):
    """
        Print log information
    """

    logger.info('Log: ' + str(message))


def error(message):
    """
        Print error information
    """

    logger.error('Log: ' + str(message))
