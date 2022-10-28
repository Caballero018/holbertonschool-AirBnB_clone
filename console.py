#!/usr/bin/python3
"Doc"
import cmd
from models.base_model import BaseModel
from models import storage
import models


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
        args = inp.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.Classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            instance = args[0] + '.' + args[1]
            if instance in objs.keys():
                print(objs[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, inp):
        if inp:
            try:
                inpu = inp.split()
                obj_dic = storage.all()
                obje_key = inpu[0] + "." + inpu[1]
                if obje_key in obj_dic:
                    del obj_dic[obje_key]
                else:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, inp):
        if inp:
            inp = inp + "()"
            inpu = eval(inp)
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()