# Simple Interpreter
The project aims at building a simple interpreter in Python 3 by following the below guide:
https://ruslanspivak.com/lsbasi-part1/

The interpreter is just a step towards the end goal of creating an interpreted language.

## Source files
### [Completed Part-8]

#### Note:
Old source files are stored in directories with naming convention `/old/part<n>`, where n denotes the part completed. For example, `/old/part6` implies that the folder contains source files when part '6' of the tutorial is completed. Do note that the repo contains only files for major parts of the tutorial. Each directory contains a `README.md` file that explains the code in the directory. Current complete part and the code explanation is provided here.


### 1. LPI.py
This is a python module containing the Lexer, the Parser and the Interpreter (and so "LPI", get it? TBH, I couldn't come up with a better name). The interpreter can handle arithmetic operations like addition, subtraction, multiplication and division. Multi-digits and the use of parentheses are supported. Also, you can have many operations in an expression and not just one. It also ignores spaces, and hence spaces can be used between characters. 

eg: 12 + 54 * (3 + 67)

The program now represents the expression as an AST (Abstract Sybtax Tree) before evaluating the expression. This is so that, it'll be easier for the interpreter to interpret the input as we progress. The parser and interpreter are now separated and have respective classes of thier own.
Support for unary operators have been added, which allows the use of negative numbers.
eg: 12 + -45, evaluated to 12 - 45, that is, -33
    45 - -----23, evaluated to 43 + 28, that is 63

### 2. AST.py
This module defines all the tree nodes for constructing the AST before the interpreter could interpret it. A base class called `AST` is defined, from which, remaining classes (AST nodes) are derived. Currently, it has an `Operator` class for specifying the operation and a `Num` clas for the numbers.

### 3. main.py
This is the main program and it has an infinite loop with `calc> ` prompt where users could enter the expression. The expression is evaluated and the result is printed on the screen, when the user presses the Enter key. Use `CTRL + C` to exit from the program.

## Execution

Run `python3 main.py` and enter the expression at the `calc> ` prompt.