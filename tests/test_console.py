#!/usr/bin/python3
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
            self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("create MyClass")
            self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show")
            self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    def test_show_invalid_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show MyClass")
            self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    def test_show_no_instance_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel 456")
            self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    def test_destroy_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    def test_destroy_invalid_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy MyClass")
            self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    def test_destroy_missing_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    def test_destroy_no_instance_found(self):
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy BaseModel 456")
            self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")
            
    def test_do_all_invalid_class(self):

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all MyClass")
            self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

if __name__ == '__main__':
    unittest.main()

