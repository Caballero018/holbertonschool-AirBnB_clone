#!/usr/bin/python3
"Doc"
import cmd


class HBNBCommand(cmd.Cmd):
    "Doc"
    prompt = "(hbnb) "
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()