#!/usr/bin/python3
"""Console test module."""
import os
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """this is test for the project"""

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertIsNone(HBNBCommand().onecmd(""))

    def test_create_missing_class_name(self):
        """Test create with no class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create")
            assert mock_stdout.getvalue() == "** class name missing **\n"
            self.assertEqual(True, True)

    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create MyClass")
            assert mock_stdout.getvalue() == "** class doesn't exist **\n"
            self.assertEqual(True, True)

    def test_show_missing_class_name(self):
        """Show test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show")
            assert mock_stdout.getvalue() == "** class name missing **\n"
            self.assertEqual(True, True)

    def test_show_invalid_class(self):
        """Show an invalid class test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show MyClass")
            assert mock_stdout.getvalue() == "** class doesn't exist **\n"
            self.assertEqual(True, True)

    def test_show_missing_id(self):
        """Show without providing id."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel")
            assert mock_stdout.getvalue() == "** instance id missing **\n"
            self.assertEqual(True, True)

    def test_show_no_instance_found(self):
        """Show invalid instance test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel 456")
            assert mock_stdout.getvalue() == "** no instance found **\n"
            self.assertEqual(True, True)

    def test_destroy_missing_class_name(self):
        """Destroy test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy")
            assert mock_stdout.getvalue() == "** class name missing **\n"
            self.assertEqual(True, True)

    def test_destroy_invalid_class(self):
        """Destroy invalid class test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy MyClass")
            assert mock_stdout.getvalue() == "** class doesn't exist **\n"
            self.assertEqual(True, True)

    def test_destroy_missing_id(self):
        """Destroy missing id test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel")
            assert mock_stdout.getvalue() == "** instance id missing **\n"
            self.assertEqual(True, True)

    def test_destroy_no_instance_found(self):
        """Destroy invalid instance."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel 456")
            assert mock_stdout.getvalue() == "** no instance found **\n"
            self.assertEqual(True, True)

    def test_do_all_invalid_class(self):
        """All invalid class test."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all MyClass")
            assert mock_stdout.getvalue() == "** class doesn't exist **\n"
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
