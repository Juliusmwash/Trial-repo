#!/usr/bin/python3
import cmd
import re
import json


class Console(cmd.Cmd):
    def do_update(self, arg):
        print(arg)
    def do_all(self, arg):
        pass
    def do_q(self, arg):
        return True

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "update": self.do_update,
            "all": self.do_all
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] == 'update' and \
                        '{' in command[1] and \
                        '}' in command[1]:
                    cmd_str = command[1].split(', ', maxsplit=1)
                    dict_str = cmd_str[1]
                    print(dict_str)
                    d_dict = json.loads(dict_str)
                    for key, value in d_dict.items():
                        k_str = str(key)
                        v_str = str(value)
                        call = "{} {} {} {}".format(
                                argl[0], cmd_str[0],
                                k_str, v_str
                                )
                        argdict[command[0]](call)
                        print("call: {}".format(call))
                    return
                    
                elif command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    call = re.sub(r',', '', call)
                    print(call)
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

if __name__ == '__main__':
    Console().cmdloop()
