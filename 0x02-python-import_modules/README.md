As witnessed when calling module2, the variable __name__ is "__main__" when called in the executed script and takes the name of the file when the script is called by another script
Every fonction inside if __name.... can't be accessed from module1
import fibo
from fibo import fib, fib2
from fibo import *
import fibo as fib
from fibo import fib as fibonacci
sys.ps1 changes the >>> ps2 ...
int(str) convert str to string
When importing the global variable are not imported if needed then can be brought this way: module.varname they can be modified an impact the functions of the imported module
dir(module) allows us to see all the names inside the module but not the variables, the list is SORTED. the functions don't start with __. ImportError: bad magic number in 'hidden_4 might occur becaue hidden_4 is in python3.8 while I use 3.12 a different version


https://docs.python.org/3/tutorial/modules.html
https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
Ctrl-B close explorer in Vscode
