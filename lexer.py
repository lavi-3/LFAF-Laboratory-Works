import re

class Lexer:
    def init(self, text):
        self.text = text

    def tokenize(self):
        # list to keep track of tokens
        tokens = []

        # split text into tokens
        text = self.text.split()

        t_index = 0

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

        return tokens