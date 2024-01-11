As witnessed when calling module2, the variable __name__ is "__main__" when called in the executed script. It takes the name of the file when the script is called by another script.
Every fonction inside if __name.... can't be accessed from module1 when module2 is executed.
import fibo
from fibo import fib, fib2
from fibo import *
import fibo as fib
from fibo import fib as fibonacci
sys.ps1 changes the >>> in python interpreter, ps2 changes ...
int(str) convert str to string.
When importing the global variable are not imported if needed they can be called this way: module.varname or import module.varname as varname to use varname. They can be modified and impact the functions of the imported module
dir(module) allows us to see all the names inside the module but not the variables, the list is SORTED. The functions don't start with '__'. ImportError: bad magic number in 'hidden_4 might occur because hidden_4 (alx's file) is in python3.8 while I use 3.12, a different version.
There are apparently no differences between import and __import__ aside from the later been able to handle more arguments like 1-.. mod_1 etc. we can also import and use the fonction in the same line as __import__('mod').func(arg)
os.write(fd, buffer) but the buffer have to be 'binary' that is why we add the b before the string like: b"text".
"import string" and "string.ascii_uppercase" let us print caped alphabet.
To write the correspondant code to the bytcode keep in mind that each block is one line of code, the name of variable is displayed between parentheses in the third column.

Ressources:
https://docs.python.org/3/tutorial/modules.html
https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments

Ctrl-B close explorer in Vscode
