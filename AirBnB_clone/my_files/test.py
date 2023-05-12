#!/usr/bin/python3
import cmd

class MyClass:
    instances = []

    @classmethod
    def all(cls):
        return cls.instances

    def __init__(self, name):
        self.name = name
        self.__class__.instances.append(self)

class MyCmd(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        name = arg.strip()
        if name:
            obj = MyClass(name)
            print(obj)

    def do_all(self, arg):
        args = arg.split()
        if args and args[0] in globals():
            cls = globals()[args[0]]
            if hasattr(cls, 'all'):
                objs = cls.all()
                print(objs)
                return
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        raise SystemExit

if __name__ == '__main__':
    MyCmd().cmdloop()

