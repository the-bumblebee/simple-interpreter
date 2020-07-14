# Part 6

### 21. calc2.py
This is a little more sophisticated interpreter that could do basic arithmetic operations like addition, subtraction, multiplication and division. Also provides support for use of parentheses and also supports multi-digits. Also, operations are not limited to just one per input but more. It also ignores white spaces and thus, spaces can be used in between characters. Negative numbers, for now, are not supported.

eg: 12 + 54 * (3 + 67)

This source file has separate classes for the lexical analyzer and the parser/interpreter. Also makes use of grammar to implement its functionality.

## Execution

Run `python3 calc2.py` and enter the expression at the `calc> ` prompt.