README 0x00-python-hello_world
to launch python interpreter: '$ python3' or '$ python3.version'
use '>>>quit()' or Ctrl-D (EOF) to leave interpreter 
Ctrl-P for previous prompt, ^P means CL editing not working
to execute command or module or script : '$ python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]'. man python3 for each flag option
to access argument we "import sys". the name of the script is in sys.arv[0] etc
to print '\' we use the raw string: "print(r"test\")"
when declaring multi-lines strin litterals we use triple quotes """. to not include a new line we use \ at the end of the line
python have a package manager: '$ pip install / install --upgrade / uninstall pckg'
print removes the quotes
to format a string it can be done with: modulo "  'hello %s' %name  ", str.format "  'test{}'.format(name)  " and f-string: "" f'test{name}'  ""
unspoken rule: always check the type of the variable even if assumed it's the correct type
inside the {} we can use :d :.2f :c etc to determine the type of the variable we are formating with
