https://docs.python.org/3/tutorial/errors.html

the syntax is:
'
try:
    blabla
except (WhatError, WhatError2):
    another blabla or pass if nothing to do
else:
    the error is not above
finally:
    executes if there is an erro or not and then re raise the previous error if any occured
'
if many except are there only the first one is executed
All the exception are in BaseException and that includes the SystemExit which is not an error, Exception is for all the errors and is a subclass of BaseException
if you like creating problems you can use: raise YourProblemError('Enter the description here trouble maker'), you can also re-raise the exception from inside the except by doing 'raise' with no argument
We can call an exception form inside another one and this is called exception chaining and can be done like this:
'
try:
    raise SyntaxError
except SyntaxError as exc:
    raise RunError from exc # or without as exc and from exc it does the same without them lol
'


