#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl-D)"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
