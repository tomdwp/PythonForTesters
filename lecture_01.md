## Objective

The purpose of this three-part class on Python is to learn how to use Python and the PyCharm editor to read and manipulate data in CSV files.

## Why Python?

* Python is free and open source
* Python is general-purpose
* Python has been designed to produce easy-to-read code, and to be efficient (fewer lines of code for solving the same problem compared to e.g. C++ or Java)
* Python works on most platforms

## Why read CSV files?

* For most people, learning by doing works better than just passively listening to theory
* CSV is a common file format, and it's humanly readable
* e.g. spreadsheets in Excel can be exported to CSV
* Focusing on reading CSV files, you can start using what you learn in each class immediately

As testers we work a lot with tabulated (spreadsheet) data - lists of defects, test data etc. - and we need to be able to easily, and quickly, read and manipulate these data.

## Introduction

In this class, we will be using the PyCharm IDE to write and execute Python code.    

## What is programming?

* When we say program we typically mean a set of instructions given to a computer in a format it can understand
* Programming languages have syntax just like human languages have grammar rules
* Different programming languages can have very different syntax
    * Java:
```java
    public void print() { 
        System.out.println("Hello World");
    }
```
    * C++:
```C++
    cout << "Hello World" << endl;
```

    * Python:
```python
    print("Hello World")
```

* We distinguish between interpreting and compiling code
* Interpreting means each statement in the code is executed directly
* Compiling means the the whole program (all lines of code) is first translated into machine-language instructions
* A script is a program that is interpreted rather than compiled
* Python counts as a scripting language

## What is an IDE?

* An IDE is an integrated development environment
* It is everything you need to write and run programs
* PyCharm is a Python IDE
* PyCharm has an extensive set of features, centred around the code editor and interpreter

## Getting started

1. Download and unpack **Python - 1.zip** into a folder Python - 1
1. Start PyCharm
1. Open folder **Python - 1** you just unpacked (click **File** --> **Open** and select the folder)
1. Open the *Python Console* by selecting **View** --> **Tool Windows** --> **Python Console** from the tool bar menu:
    ![PQA Academy > Python for Testers: Class 1 > Screen Shot 2015-10-03 at 5.08.41 PM.png]
1. You can type commands directly into the console
1. Try input the following commands, one at the time, followed by Enter
```
    >>> 2+4
    >>> 2*5
    >>> 5/2
```

What results did you get, and why?

*Tip*: You can use the up and down arrows to browse through the console history!

## Data types

A data type specifies what kind of data we are dealing with.

Some of the most commonly used data types in Python are:

* Strings (str) - "Hello"
* Integers (int) - "2"
* Floating point numbers (float) - "3.14" etc.

Python will automatically assign a type to our input, and we can use the `type()` function to display the data type:

```
        >>>type("Hello")
        <type 'str'>
        >>>type(2)
        <type 'int'>
        >>>type(3.14)
        <type 'float'>
```

Python can't handle different data types in the same command


But, we can change the type!

* For example, the function `int()` converts our input to an integer, and `str()` converts the input to a string:

```
        >>>int("3")
        3
        >>>str(3)
        '3'
```

This is called typecasting.

## Print

The `print()` function displays values on the screen:

```
    >>>print("Hello world")
    Hello world
    >>>print(2+3)
    5
```

You have to use quotation marks to print strings.

The expression inside the parenthesis is evaluated before print is invoked.

You can join (concatenate) multiple strings together using "+":

```
    >>>print("Hello " + "world")
    Hello world
```    

What happens when you try to print a string and a number? Try this command:

```
    >>>print("The year is " + 2015)
```

Since they are different data types, Python gets confused

## Writing scripts

Entering commands one-by-one in the console is not a great way to build a program, so instead we write our code in the code editor. The console is very convenient for trying separate statements before we enter them into the script in the code editor.

*Note: indentation is very important in Python - wrong indentation will create an error, even if the code is correct!*

## Create a new script file

You can create a new Python file by clicking **File** --> **New...** --> **Python file** and entering any file name. All Python files must have the file extension `.py`.

Execute, or run, the code by clicking the green arrow on line one

![PQA Academy > Python for Testers: Class 1 > Screen Shot 2015-10-03 at 5.19.56 PM.png]

Running the code will open a new window, the Run window

Switch between windows by clicking on the name bar

![PQA Academy > Python for Testers: Class 1 > Screen Shot 2015-10-03 at 5.21.50 PM.png]

## Comments

Any text preceded by "#" is ignored by Python, and that's how we enter comments

```python
    # This is a comment
    # And another comment
```

Make sure to use comments extensively to explain your code!

## Exercise 1

Create a script that displays "Hello world" on the screen - and don't forget the comments!

Exercise01.py

## Variables

Variables are reserved memory locations that store values

We assign values to the variables using the equals sign "="

It helps some people to read the equal sign as "gets" instead of "equals"

Once a variable has been assigned it can be changed, try creating this script and running it in your console

```python
    # year 'gets' the value 2015
    year = 2015
    print(year)
     
    # year 'gets' the value 2016
    year = 2016
    print(year)
```

You can also assign multiple variables the same value all at once, or assign multiple variables multiple values on one line

```python
    # a, b and c all have the value of 5
    a = b = c = 5
     
    # d has a value of 1, e has a value of 2 and f has a value of 'hello'
    d, e, f = 1, 2, "hello"
```

Try the statements above in the console

## Reading input

Sometimes we want the user to give us values, or input
`raw_input()` accepts a string and returns a string

You can ask a user a question and have the user respond, try running this code in the console:

```python
    raw_input("What year is it?")
```

For Python to remember data that the user enters, we need to assign it to a variable

```python
    year = raw_input("What year is it?")
    print(year)
```

## Exercise 2

* Create a script that asks the user to enter the month (e.g. September) and day of the month (e.g. 12) and displays "Today is September 12" on the screen

* Exercise02.py

## Functions

* Functions are groups of instructions that we can re-use
* Using functions reduces redundancy
* Functions can take arguments and can return values

```
    >>> def add(x,y) :
    ...	return x + y
    ...
    >>> add(4,5)
    9
```

## Exercise 3

* Create a script that converts pounds to kg
* Hint: 1 pound = 0.453592 kg
* Exercise03.py