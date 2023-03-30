# Topic: Lexer
## Course: Formal Languages & Finite Automata
### Author: Cozlov Valeria, FAF-213
## Theory 
<p>
In computer science and natural language processing, lexical analysis is a technique used to recognize and examine the individual words or tokens that make up a piece of text.

The text is divided into smaller units like words, punctuation, and other symbols in this process, and these units are then categorized according to their kind, frequency, and connections with other units in the text. This aids in determining the text's patterns, structures, and meaning.

Lexical analysis' goal is to give the text a structured form that computers can quickly process. This is helpful for a variety of things, such as text classification, machine translation, and search engines.

Specialized software tools and algorithms are employed to do lexical analysis. To recognize and categorize the different text components, these technologies frequently use methods like tokenization, finite state machines, and regular expressions.

Overall, lexical analysis is a key method in the field of natural language processing and is essential for giving robots the ability to comprehend and interpret human language.

</p>

### How does the Lexer work?
Tokens are produced by the lexer and sent to the parser for further processing. The parser creates a parse tree, which depicts the structure of the program, after analyzing the program's structure using the grammar of the programming language.

## Objectives:
1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation description
This approach tokenizes a given source code using a straightforward lexer that was written in Python. It recognizes several token kinds, including variable declarations, numbers, identifiers, operators, and separators, using regular expressions.
```    
  def init(self, text):
        self.text = text

    def tokenize(self):
        # list to keep track of tokens
        tokens = []

        # split text into tokens
        text = self.text.split()

        t_index = 0
```
Lexical analysis is being implemented in this code for a programming language. It accepts a text string as input and iterates through each of its tokens one at a time, categorizing them according to their category.

The code adds the term "var" to the list of tokens after first identifying variable declarations. Then, it adds numbers to the list along with their type and uses regular expressions to identify them. Identifiers, operators, and separators all function in the same way.

Unrecognized token: token name throws a ValueError if any of the aforementioned requirements are not met by a token.
``` 
# iterate through tokens
        while t_index < len(text):
            token = text[t_index]

            # recognize a declaration
            if token == "var":
                tokens.append(['DECLARATION', token])
                t_index += 1
                continue

            # recognize an integer
            elif re.match('^[-+]?[0-9]+$', token):
                if token[-1] == ";":
                    tokens.append(['INTEGER', int(token[:-1])])
                else:
                    tokens.append(['INTEGER', int(token)])
                t_index += 1
                continue

            # recognize an identifier
            elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', token):
                if token[-1] == ";":
                    tokens.append(['IDENTIFIER', token[:-1]])
                else:
                    tokens.append(['IDENTIFIER', token])
                t_index += 1
                continue

            # recognize an operator
            elif token in "+-=*/":
                tokens.append(['OPERATOR', token])
                t_index += 1
                continue

            # recognize a separator
            elif token == ";":
                tokens.append(['SEPARATOR', token])
                t_index += 1
                continue

            # unrecognized token
            else:
                raise ValueError("Unrecognized token: {}".format(token)) 
  ```
                
A list of tokens, each of which is represented as a tuple containing the token type and the corresponding value, is the result of this code.

## Conclusion
In conclusion, lexical analysis, which entails dissecting the source code into smaller tokens and categorizing them, is a crucial component of programming language processing. A program known as a lexer or tokenizer conducts lexical analysis and produces a list of tokens that can be used in subsequent processing.

Developers may quickly do lexical analysis on their code and produce a list of tokens that can be used for additional processing such as parsing, interpretation, and execution of the code by building a lexer in Python. Overall, building a lexer in Python can make it much simpler to design tools and programs that use programming languages.
____

