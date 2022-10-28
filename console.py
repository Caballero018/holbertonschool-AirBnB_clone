#!/usr/bin/python3
"Doc"
import cmd
from models.base_model import BaseModel
from models import storage


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
        if inp:
            try:
                inp = inp + "()"
                inp = eval(inp)
                print(inp.id)
                inp.save()
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, inp):
        if inp:
            try:
                inpu = inp.split()
                inpu[0] = inpu[0] + "()"
                inpu[0] = eval(inpu[0])
                if inpu[0].id == inpu[1]:
                    print(inpu[0])
                else:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, inp):
        if inp:
            try:
                inpu = inp.split()
                inpu[0] = inpu[0] + "()"
                inpu[0] = eval(inpu[0])
                if inpu[0].id == inpu[1]:
                    del inpu[0].id
                else:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

