#!/usr/bin/python3
"Doc"
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd, BaseModel):
    "Doc"
    prompt = "(hbnb) "

    class_id = {
        "User": "user",
        "BaseModel": "base_model",
        "State": "state",
        "City": "city",
        "Amenity": "amenity",
        "Place": "place",
        "Review": "review"}

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

    def do_show(self, line):
        """Prints the string representation of an
            instance based on the class name and id"""
        line_read = line.split(" ")
        if line_read == ['']:
            print("** class name missing **")
            return
        elif line_read[0] not in HBNBCommand.class_id.keys():
            print("** class doesn't exist **")
            return
        elif len(line_read) < 2:
            print("** instance id missing **")
            return
        conct = line_read[0] + "." + line_read[1]
        if not models.storage._FileStorage__objects.get(conct):
            print("** no instance found **")
        else:
            obj = models.storage._FileStorage__objects[conct]
            print(obj)

    def do_all(self, inp):
        if inp:
            inp = inp + "()"
            inpu = eval(inp)
        

        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

