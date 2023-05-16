#!/usr/bin/python3
import unittest
from console import parse_cmd
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch



class TestConsole(unittest.TestCase):

    """
    TestConsole parses the unittest testcase
    TestConsole tests the console.py module
    """

    # test basemodel commands
    def test_parse_cmd(self):
        """
        test case for th basemodel commands
        checking if the values parsed by users are valid
        """
        self.assertEqual(parse_cmd("create BaseModel"), ['create', 'BaseModel'])
        self.assertEqual(parse_cmd("create BaseModel id=123"), ['create', 'BaseModel', 'id=123'])
    
    # test other command test cases
    def test_parses_comands(self):
        """
        test case for input in the cmd
        checking if the arg values are valid
        """
        # Test with input "{arg1}"
        result = parse_cmd("{arg1}")
        self.assertEqual(result, ["arg1"])

        # Test with input "[arg1]"
        result = parse_cmd("[arg1]")
        self.assertEqual(result, ["arg1"])

        # Test with input "command"
        result = parse_cmd("command")
        self.assertEqual(result, ["command"])

        # Test with input "command [arg1]"
        result = parse_cmd("command [arg1]")
        self.assertEqual(result, ["command", "arg1"])

        # Test with input "command {arg1}"
        result = parse_cmd("command {arg1}")
        self.assertEqual(result, ["command", "arg1"])

