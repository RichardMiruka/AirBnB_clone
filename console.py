#!/usr/bin/env python3
"""
Module that contains the entry of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_show(self, arg):
        """
        print string representation of instance based on class name
        """

        if not arg:
            print("** class name missing **")
            return
        line = arg.split(' ')
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for ke, value in objs.items():
                name = value.__class__.__name__
                obj_id = value.id
                if name == line[0] and obj_id == line[1].strip('"'):
                    print(value)
                    return
            print("**no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        """

        if not arg:
            print("** class name missing **")
            return
        line = arg.split(' ')
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("**  instance id missing **")
        else:
            objs = storage.all()
            for key, value in objs.items():
                name = value.__class__.__name__
                obj_id = value.id
                if name == line[0] and obj_id == line[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        prints all string representation of all instances based on
        or not on the class name
        """
        if not arg:
            print("** class name missing **")
            return

        line = arg.split(' ')
        if line[0] not in HBNBCommand.model_classes:
            print("** class doesn't exist **")
            return
        else:
            objs = storage.all()
            inst_list = []
            for key, value in objs.items():
                name = value.__class__.__name__
                if name == line[0]:
                    inst_list += [value.__str__()]
            print(inst_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
