#!/usr/bin/python3

from cmd import Cmd
from typing import IO
from models.user import BaseModel
"""
HBNBCommand class is command-line interpreter for  managing 
public instance attributes:
    prompt: str - the prompt displayed to the user

public instance methods:
    help(self, line): Display a list of documented command.
    do_quit(self, line): Quit command to exit the program.
    do_EOF(self, line): EOF command to exit the program
    default(self, line): Handles the command if its not recognized
    emptyline(self): Overrides the default behavior when empty line is entered.
"""
class HBNBCommand(Cmd):
    # intro = "Welcome to HBNBCommand. Type help or ? to list commands.\n"
    prompt = "(hbnb) "

    def __init__(self):
        """Initializes a new instance of HBNBCommand class."""
        super().__init__()
        self.usrers = {}

    def help(self, line):
        """Display a list of documented command.
        """
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
        """Handles the command if its not recognized
        """
        return super().default(line)

    def emptyline(self):
        """ Overrides the default behavior when empty line is entered.
        """
        print(end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

