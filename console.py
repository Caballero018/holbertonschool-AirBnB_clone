#!/usr/bin/python3
"Doc"
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd, BaseModel):
    "Doc"
    prompt = "(hbnb) "

    def do_quit(self, inp):
        "Doc"
        return True

    def help_quit(self):
        "Doc"
        print("Quit command to exit the program")

    def do_EOF(self, inp):
        "Doc"
        return True

    def help_EOF(self):
        "Doc"
        print("Quit command to exit the program")

    def do_create(self, inp):
        if inp == "BaseModel":
            inp = BaseModel()
            print(inp.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
