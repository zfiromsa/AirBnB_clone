#!/usr/bin/python3

"""HBNBCommand class is command-line interpreter for managing."""

from cmd import Cmd
from typing import IO
from models.user import BaseModel

class HBNBCommand(Cmd):
    """
    HBNBCommand class is command-line interpreter for managing.

    public instance attributes:
        prompt: str - the prompt displayed to the user.
    
    public instance methods:
        help(self, line): Display a list of documented command.
        do_quit(self, line): Quit command to exit the program.
        do_EOF(self, line): EOF command to exit the program.
        default(self, line): Handles the command if its not recognized.
        emptyline(self): Overrides the default behavior when empty line is entered.
    """

    prompt = "(hbnb) "

    def __init__(self):
        """Initialize a new instance of HBNBCommand class."""
        super().__init__()
        self.usrers = {}

    def help(self, line):
        """Display a list of documented command."""
        print("\nDocumented commands (type help <topic>):")
        print("========================================")
        print("EOF  help   quit")

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True
    
    def default(self, line):
        """Handle the command if its not recognized."""
        return super().default(line)

    def emptyline(self):
        """Override the default behavior when empty line is entered."""
        print(end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

