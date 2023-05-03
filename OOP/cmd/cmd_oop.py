#!/usr/bin/env python3
import cmd


class HelloWorld(cmd.Cmd):
    """simple command processor example"""
    prompt = '(hbnb) '

    def do_greet(self, person):
        if person:
            print("Hi,", person)
        else:
            print("Hi")

    def help_greet(self):
        print('\n'.join([ 'greet [person]', 'Greet the named person',]))

    def do_EOF(self, line):
        """End program cleanly when CTRL+D is pressed"""
        return True

    def do_quit(self, line):
        """Exit interpreter"""
        return True

    def postloop(self):
        print


if __name__ == '__main__':
    HelloWorld().cmdloop()
