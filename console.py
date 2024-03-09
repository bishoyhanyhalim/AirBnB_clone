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
        """Creates a new instance of a given class,save it and prints its id"""
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
                if name.split('.')[0] == args[0]:
                    print_f.append(str(obj))

        print(print_f)

    def do_update(self, arg):
        """this func to make update of id"""
        args = arg.split()
        obj = storage.all()

        if not args:
            print("** class name missing **")
            return False

        elif args[0] not in storage.class_mapping:
            print("** class doesn't exist **")
            return False

        elif len(args) == 1:
            print("** instance id missing **")
            return False

        elif len(args) == 2:
            print("** attribute name missing **")
            return False

        elif (f"{args[0]}.{args[1]}") not in obj.keys():
            print("** no instance found **")
            return False

        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        elif len(args) == 4:
            """for update value"""
            objO = obj[f"{args[0]}.{args[1]}"]

            if args[2] in objO.__class__.__dict__.keys():
                type_value = type(objO.__class__.__dict__[args[2]])
                objO.__dict__[args[2]] = type_value(args[3])

            else:
                objO.__dict__[args[2]] = args[3]

        elif type(eval(args[2])) == dict:
            """for update value"""
            objO = obj[f"{args[0]}.{args[1]}"]

            for k, v in eval(args[2]).items():
                if (k in objO.__class__.__dict__.keys() and
                        type(objO.__class__.__dict__[k]) in {str, int, float}):
                    type_value = type(objO.__class__.__dict__[k])
                    objO.__dict__[k] = type_value(v)
                else:
                    objO.__dict__[k] = v

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
