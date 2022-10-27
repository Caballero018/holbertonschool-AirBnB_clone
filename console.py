#!/usr/bin/python3
"Doc"
import cmd


class HBNBCommand(cmd.Cmd):
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
    
    def do (sef, inp):
        return

    def help_EOF(self):
        "Doc"
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
