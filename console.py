#!/usr/bin/python3
"""
The Console Module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """the functionality of HBNB console"""
    prompt = "(hbnb)"
           
    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def default(self, arg):
        """Default behaviour for cmd module when input is invalid"""
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

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        exit()

    def do_quit(self, argv):
        """Quit command to exit the program"""
        exit()

   
if __name__ == "__main__":
    HBNBCommand().cmdloop()
