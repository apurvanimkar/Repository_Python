#Modules can be imported by other modules.
# hello.py
import hello
hello.say_hello()

#Specific functions of a module can be imported.
#hello.py
from hello import say_hello
say_hello()

#Modules can be aliased.
# hello.py
import hello as ai
ai.say_hello()

#A module can be stand-alone runnable script.
# hello.py
if __name__ == '__main__':
from hello import say_hello
say_hello()