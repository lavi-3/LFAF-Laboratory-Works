# Parser & Building an Abstract Syntax Tree
**Course:** Formal Languages & Finite Automata  
**Author:** Cozlov Valeria \
**Variant:** 13
## Grammar
G=(VN, VI, P, S) Vn={S, A, B, C, D} VT={a, b}
P={ 
1. S → aB
2. S → DA
3. A → a
4. A → BD
5. A → bDAB
6. B → b
7. B → BA
8. D → ε
9. D → BA
10. C → BA}
## Theory
Parsing is the process of obtaining syntactic meaning from a given text, such as a programming language expression. Building a hierarchical structure to depict the relationships between the text's many components includes evaluating the text. The term "parse tree" refers to this hierarchical arrangement.

The Abstract Syntax Tree is another helpful illustration of the text's structure in addition to the parse tree (AST). The AST abstracts away superfluous details while capturing the text's important components. It arranges the text's elements in layers of abstraction that match to the constructs or entities of the original text.

The AST shows to be especially useful throughout various stages of compilation and program analysis. For purposes like semantic analysis, optimization, and code generation, it offers a succinct and organized representation of the program's syntax.

To sum up, parsing and the generation of an AST are essential steps for understanding and working with text, particularly in the context of programming languages and compilation processes.

## Objectives

1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description

### Parser Class
The Parser uses a recursive descent parser to break down expressions into their component tokens. It manages all kinds of operations and values while creating a hierarchical representation of the expressions using nodes.
The Parser object is initialized with a list of tokens by the __init__ method. It initializes the current token (self.current token) as None and sets the list of tokens as an instance variable (self.tokens). The first token from the list is then set as the current token by using the following procedure.

The next method advances to the following input list token. Using pop(0), it selects the first token from the list and assigns it to self. current token. It sets self if the token list is empty. to None for current token.

The expression method is called by the parse method, which also prints a message to initiate the parsing process.

An expression with terms is parsed using the expression technique. It first prints a message stating that the phrase is being parsed. The term method is then invoked in order to parse the term. When the current token is not None and its type is either "PLUS" or "MINUS," the procedure enters a while loop that runs indefinitely. It verifies the type of the current token inside the loop. If it is 'PLUS', it continues on to the next token, modifies the expr variable to represent an addition node, and outputs a message indicating that it is parsing an addition operation (('ADD', expr, self.term())). It executes a similar operation for subtraction if the current token type is "MINUS." The procedure then returns the expr at the end of the while loop.

The term method parses a term involving factors. It first prints a message indicating that it is parsing the factor. It then calls the factor method to parse the factor. The method enters a while loop that continues as long as the current token is not None and its type is either 'TIMES' or 'DIVIDE'. Inside the loop, it checks the type of the current token. If it is 'TIMES', it prints a message indicating that it is parsing a multiplication operation, moves to the next token, and updates the term variable to represent a multiplication node (('MUL', term, self.factor())). If the current token type is 'DIVIDE', it performs a similar process for division. After the while loop ends, the method returns the term.

A factor, which can be either a numeric number or an enclosed expression contained in parentheses, is parsed using the factor technique. If the current token type is "NUMBER," it extracts the value from the numeric token, outputs a message to say that it is parsing a number, moves on to the next token, and returns a node that represents the numeric value (("NUM"], value)). If the current token type is a closing parenthesis ('RPAREN'), it proceeds to the next token, parses the enclosed expression recursively by invoking the expression method, prints a message indicating that it is doing so, then moves to the next token and returns the enclosed expression's parsed value. If neither the current token type nor "NUMBER,"

### Interpreter
Interpreter class is responsible for interpreting a parse tree and performing calculations based on its nodes. Here's an explanation of what the code does:
The Interpreter class has an __init__ method that initializes an empty dictionary self.variables to store variables.
The interpret method takes a parse tree as input and interprets it to compute a result. It starts by extracting the type of the root node from the parse tree.
•	If the node type is 'NUM', it means the node represents a numeric value. The method returns the numeric value by converting it to a float.
•	If the node type is 'ADD', 'SUB', 'MUL', or 'DIV', it means the node represents an arithmetic operation. The method recursively interprets the left and right children of the node by calling the interpret method on them. It then performs the corresponding arithmetic operation (+, -, *, /) on the computed values and returns the result.
•	If an invalid node type is encountered, the method raises a ValueError with a message indicating the invalid node type.
In summary, the Interpreter class provides functionality to interpret a parse tree and perform calculations based on its nodes. It supports numeric values and basic arithmetic operations. When given a valid parse tree, the interpret method evaluates the expression represented by the tree and returns the computed result.


# Conclusion
In conclusion, the parser shows how to extract syntactical meaning from text, especially from phrases used in programming languages. In order to evaluate expressions and carry out calculations, it creates a parse tree and works in tandem with an interpreter. Parsers are significant in software development and compiler design since they are required for activities like semantic analysis and code creation.
