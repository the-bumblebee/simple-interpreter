# Simple Interpreter
The project aims at building a simple interpreter iin Python 3 by following the below guide:
https://ruslanspivak.com/lsbasi-part1/

The interpreter is just a step towards the end goal of creating an interpreted language.

## Source files

#### Note:
[] within each source file section shows which all parts of the guide need to be completed beginning from part 1, so as to write the corresponding source file.

### 1. old/calc1.py
#### [Completed Part-1]
This is a very simple and easy to understand interpreter that evaluates addition of two single digit numbers. 
eg: 1+1, 2+3 and so on.

Please do note that spaces arent allowed between the characters and if a space is encountered the program raises an exception.

### 2. old/calc2.py
#### [Completed Part-6]
This is a little more sophisticated interpreter that could do basic arithmetic operations like addition, subtraction, multiplication and division. Also provides support for use of parentheses and also supports multi-digits. Also, operations are not limited to just one per input but more. It also ignores white spaces and thus, spaces can be used in between characters.
eg: 12 + 54 * (3 + 67)

This source file has separate classes for the lexical analyzer and the parser/interpreter. Also makes use of grammar to implement its functionality.

### 3. main.py
#### [Completed Part-7]
This program represents an expression as an AST (Abstract Sybtax Tree) before evaluating the expression. AST is a data structure required in parsing the high level language. The parser and interpreter are now separated and have respective classes of thier own. Functionality remains same as that of calc2.py.
