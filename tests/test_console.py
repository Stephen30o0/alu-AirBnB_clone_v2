#!/usr/bin/python3
''' Test console'''


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console.do_destroy("all")

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create UnknownClass")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('create BaseModel name="My_house" number=123 price=2.5')
            output1 = output.getvalue()
            self.assertTrue(len(output1) > 0)
            self.assertTrue("BaseModel" in output1)
            self.assertTrue("My house" in output1)
            self.assertTrue("123" in output1)
            self.assertTrue("2.5" in output1)

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create BaseModel name='My\"big\"house' number=123 price=2.5")
            output1 = output.getvalue()
            self.assertTrue(len(output1) > 0)
            self.assertTrue("BaseModel" in output1)
            self.assertTrue("My\"big\"house" in output1)
            self.assertTrue("123" in output1)
            self.assertTrue("2.5" in output1)

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create BaseModel name=My_little_house number=123 price=2.5")
            output1 = output.getvalue()
            self.assertTrue(len(output1) > 0)
            self.assertTrue("BaseModel" in output1)
            self.assertTrue("My little house" in output1)
            self.assertTrue("123" in output1)
            self.assertTrue("2.5" in output1)

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create BaseModel name='My house' number=123 price=2.5")
            output1 = output.getvalue()
            self.assertTrue(len(output1) > 0)
            self.assertTrue("BaseModel" in output1)
            self.assertTrue("My house" in output1)
            self.assertTrue("123" in output1)
            self.assertTrue("2.5" in output1)

        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create BaseModel name='My house' number=123 price=2.5 extra_param=ignored")
            output1 = output.getvalue()
            self.assertTrue(len(output1) > 0)
            self.assertTrue("BaseModel" in output1)
            self.assertTrue("My house" in output1)
            self.assertTrue("123" in output1)
            self.assertTrue("2.5" in output1)
            self.assertFalse("extra_param" in output1)

if __name__ == '__main__':
    unittest.main()
