#!/usr/bin/env python3
"""
this module test consol module using unittest.TesCase and Mock module
"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class test_console(unittest.TestCase):
    """
    This is tests for console methods
    """

    def setUp(self):
        with patch('sys.stdout', new=StrinIO()) as f:
            HBNBCommand().onecmd("help show")
