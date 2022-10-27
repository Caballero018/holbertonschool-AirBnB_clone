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
        if len(inp) == 0:
            print("** class name missing **")
            return
        args = split(inp)
        if args[0] != 'BaseModel':
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                out = "{}.{}".format(args[0], args[1])
                if out not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[out])
        except IndexError:
            print("** instance id missing **")
            return


    def to_destroy(self, inp):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
