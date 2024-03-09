#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter."""
import cmd
import sys
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl-D)"""
        print()
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a given class, saves it and prints it's id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.class_mapping:
            print("** class doesn't exist **")
        else:
            new_obj = storage.class_mapping[args[0]]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.class_mapping:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            name = f"{args[0]}.{args[1]}"
            if name in storage.all():
                print(storage.all()[name])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.class_mapping:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            name = f"{args[0]}.{args[1]}"
            if name in storage.all():
                del storage.all()[name]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        print_f = [] 
        if not arg:
            for name, obj in storage.all().items():
                print_f.append(str(obj))
        else:
            args = arg.split()
            if args[0] not in storage.class_mapping:
                print("** class doesn't exist **")
                return
            for name, obj in storage.all().items():
                if name.split('.')[0]  == args[0]:
                    print_f.append(str(obj))

        print(print_f)
     

if __name__ == '__main__':
    HBNBCommand().cmdloop()
