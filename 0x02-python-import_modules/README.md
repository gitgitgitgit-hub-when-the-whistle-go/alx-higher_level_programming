As witnessed when calling module2, the variable __name__ is "__main__" when called in the executed script and takes the name of the file when the script is called by another script
Every fonction inside if __name.... can't be accessed from module1
import fibo
from fibo import fib, fib2
from fibo import *
import fibo as fib
from fibo import fib as fibonacci
sys.ps1 changes the >>> ps2 ...
int(str) convert str to string

https://docs.python.org/3/tutorial/modules.html

Ctrl-B close explorer in Vscode
