for dogst*ng leave 2 lines after nodule discription

when defining a class:
""" blabla
Args:
    arg1: ....
Atrributes:
    __attr1: .... """

same goes for each function but add:
    Returns:
        int: The product of a and b.
    """

if raise them:
    Raises:
        ValueError: if dsfsadfasdfsadf

Some functions like getter and setter and init can get away with not having docstring anyways frak docstr*ng anyway

Now to the serious part xDDD:

There are 2 methods to write programs: procedural and oriented object programming.
Procedural consist of writing functions in blocks while oriented object programming consists of wrapping this functions in a class.
An object is an instance of a class.
Variables that belong to an object or a class called fields, functions that belong to an object are called methods. Fields and methods are called attributes.
The fields can belong to an instance or to the class itself, the first is called instance variable while the later is called class variable.

Methods differs from normal function by having the first variable “self” or named otherwise. When calling the method, Python will interpret it as follows: 
myobject.method1(var1, var2, …) = method1(myobject, var1, var2)
The __init__ function allows us to initialize our object with values. Having the self.var = var do not create problem since the first one is attached to self.
We can define methods that belong to a class and not an object as classmethod or staticmethod: my_method = classmethod(my_method). A regular method(self, ...) is bound to an instance, a classmethod(cls, …) is bound to a class and a static method(var1, var2 ...) is bound to nothingh, it just have a logical connection to the class. We can designate in the code by adding @classmethod or @staticmethod in the line before the definition of our method.

The attributes of an instance are stored in a dictionary and can be accessed with: instance.__dict__
The __str__ and __repr__ are two methods that convert object to string. If no function is defined, Python uses the default str(element). This is used in print: print(obj) is print(__str__(obj))
The method (destructor) __del__() allows us to delete the instance. If it’s not defined then default one will be used.

There are 3 types of attributes: public, protected and private.
Public attributes are accessible inside and outside class definition. attribute1
Protected shouldn’t be used outside of class definition inside of subclass definition. _attributes2
Private are not readable or writable to expect in class definition itself. __attribute3

Data encapsulation is to handle data with getters and setters so it can’t be accidentally changed.

But apparently pythoneers like to auto-contratry, so we are going to play it private but in the same time public and this can be achived by using decorators and private attributes. This will allow us to raise errors in case data is not conveniente

how to use decoration: https://python-course.eu/oop/properties-vs-getters-and-setters.php
