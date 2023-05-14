#!/usr/bin/python3
"""
The Console Module.
"""
import cmd
import re
import sys
import shlex
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse_cmd(argv: str) -> list:
    """
    Parse or split a string (argv) based on some pattern
    example, spaces, brackects

    :param arg: string
    :return:  a list of words representing the parsed string
    """
    braces = re.search(r"\{(.*?)}", argv)
    brackets = re.search(r"\[(.*?)]", argv)
    if not braces:
        if not brackets:
            return [i.strip(",") for i in shlex.split(argv)]
        else:
            var = shlex.split(argv[:brackets.span()[0]])
            retval = [i.strip(",") for i in var]
            retval.append(brackets.group())
            return retval
    else:
        var = shlex.split(argv[:braces.span()[0]])
        retval = [i.strip(",") for i in var]
        retval.append(braces.group())
        return retval


def check_args(args):
    """
    checks if args is valid
    Args:
        args (str): the string containing the arguments passed to a command
    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse_cmd(args)
    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):

    """Command line interpreter for HBNB application."""

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    classes = {
        "BaseModel": BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop
    # an empty line +
    # enter shouldn’t execute anything

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    # checks when input is invalid
    def default(self, arg):

        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    # handles the EOF to exit program
    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        return True

    # handles the quit action of the program
    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_create(self, arg):
        """
        Create an Instance of a class
        [USAGE]: create <classname>
        [Return]: id of the created class
        """
        # handles the create command
        # creates a new class instance & prints its id
        # arg represents the class being called

        args = check_args(arg)
        if args:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        [USAGE]: show <classname> <id>
        """
        # handles the show command
        # displays a string representation of a class instance

        args = re.findall(r'\w+', arg)

        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        [USAGE]: destroy <classname> <id>
        """
        # handles the destroy command
        # destroys the class instance of a given id

        args = re.findall(r'\w+', arg)

        # prints if the classname is missing
        if not args:
            print("** class name missing **")
            return

        # prints if classname doesn't exist
        class_name = args[0]
        if class_name not in storage.__class__():
            print("** class doesn't exist **")
            return

        # prints if the instance id is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        # check instances & deletes instance from storage

        instance_id = args[1]
        key = class_name + "." + instance_id
        instances = storage.all()

        # saves the changes in the code

        if key not in instances:
            print("** no instance found **")
            return

        del instances[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        [USAGE]: all <classname>
        """
        # print the string representation of all the classes instance
        # represents the all command
        # prints if no classname is provided
        arg_list = shlex.split(arg)
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects if arg_list[0] in str(obj)])

    def do_count(self, arg):
        """
        the action counts the number of instances of a class.
        Usage: <class name>.count()
        """
        arg1 = parse_cmd(arg)
        count = 0
        for obj in storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        [USAGE]: update <classname> <id> <attribute name> "<attribute value>"
        """
        # handles the update command
        # updates an instance based on the class name & id
        # saves the change into the JSON file

        arg_list = check_args(arg)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")
            storage.save()


# the cmdloop call starts the interpreter
# prevent code from being executed when the module is imported
# cmdloop() method will continue to prompt the user for input
# til they exit the interpreter.
if __name__ == "__main__":
    HBNBCommand().cmdloop()
