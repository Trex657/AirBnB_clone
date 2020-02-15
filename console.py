#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

"""
    bla bla bla
"""


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""  
        return True

    def do_EOF(self, args):
        """Exit with a signal EOF"""
        return True

    def emptyline(self):
        """"""
        pass

    def do_create(self, args):
        """"""
        if args == "":
            print("** class name missing **")
            return
        try:
            cmmd = args.split()
            instance = eval(cmmd[0])()
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """"""
        pass

    def do_destroy(self, args):
        """"""
        pass

    def do_all(self, args):
        """"""
        pass

    def do_update(self, args):
        """"""
        pass

if __name__ == '__main__':
    """
        Call The Shell
    """
    HBNBCommand().cmdloop()
