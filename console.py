#!/usr/bin/python3
"Doc"
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd, BaseModel):
    "Doc"
    prompt = "(hbnb) "
    Classes = ["BaseModel", "User"]

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
                del objs[instance]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, inp):
        args_str = inp.split()
        if not inp or args_str[0] in HBNBCommand.Classes:
            str_l = []
            objs = storage.all()
            for ins in objs.values():
                str_l.append(ins.__str__())
            print(str_l)
        else:
            print("** class doesn't exist **")

    def do_update(self, inp):
        args = inp.split()
        try:
            if not inp:
                print("** class name missing **")
            if not inp or args[0] in HBNBCommand.Classes:
                if len(args) == 1:
                    print("** instance id missing **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                objs = storage.all()
                instance = args[0] + '.' + args[1]
                if instance in objs.keys():
                    setattr(objs[instance], args[2], eval(args[3]))
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except IndexError:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()