#!/usr/bin/env python3
"""
Module that contains the entry of the command interpreter
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class defination of the consol
    """

    prompt = '(hbnb) '

    model_classes = ['BaseModel']

    def do_quit(self, line):
        """ quits the program
        """

        return True

    def do_EOF(self, line):
        """exits the program when end of file is reached
        """
        print('')

        return  True

    def help_help(self):
        """ used to show description of command called"""

        print("Describes a given command")

    def emptyline(self):
        """doesn't execute anything when empty line is entered
        """

        pass
    def do_create(self, model_type):
        """ creates a new instance of BaseModel
        """

        if not model_type:
            print("** class name missing **")
            return
        elif model_type not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
            return
        else:
            dct = {'BaseModel': BaseModel}

        myModel = dct[model_type]()
        print(myModel.id)
        myModel.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
