#!/usr/bin/python3

from cmd import Cmd
from typing import IO
from models.user import BaseModel

class HBNBCommand(Cmd):
    # intro = "Welcome to HBNBCommand. Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    file = None  # Used to demonstrate the use of file input/output


    def __init__(self):
        super().__init__()
        self.usrers = {}

    def help(self, line):
        print("\nDocumented commands (type help <topic>):")
        print("========================================")
        print("EOF  help   quit")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    
    def default(self, line):
        return super().default(line)

    def emptyline(self):
        print(end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

