README 0x00-python-hello_world
to launch python interpreter: '$ python3' or '$ python3.10'
use '>>>quit()' or Ctrl-D (EOF) to leave interpreter 
Ctrl-P for previous prompt, ^P means CL editing not working
to execute command or module or script : '$ python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]'. man python3 for each flag option
to access argument we "import sys". the name of the script is in sys.arv[0] etc
to print '\' we use the raw string: "print(r"test\")"
when declaring multi-lines string litterals we use triple quotes """. to not include a new line we use \ at the end of the line
python have a package manager: '$ pip install / install --upgrade / uninstall pckg'
print removes the quotes
to format a string it can be done with: modulo "  'hello %s' %name  ", str.format "  'test{}'.format(name)  " and f-string: "" f'test{name}'  "", in case format have multiple argument we can define the order of arguments inside the brackets, for debugging we can use "print(f"variable =")"
unspoken rule: always check the type of the variable even if assumed it's the correct type
inside the {} we can use :d :.2f :c etc to determine the type of the variable we are formating with
No string literals means no f"" or "".format because even with empty quotes it count as literal
the zen of python is printed with "import this"
the module sys contains write fonctions that allows us to write on stdout.write or stderr.write. it also contains sys.exit() that allows us to determine the status code to be echoed.
the python interpreter first compile the script then interprete line per line form the bytecode script (.pyc).'$python3 -m compileall -b filename'  or "import py_compile" and "py_compile.compile(file)" to compile to bytecode.
to read bytecode we use "import dis" and then "dis.dis(function or file without .py)". to understand bytecode: https://www.youtube.com/watch?v=mE0oR9NQefw . 