class Parser:
    def __init__(self, tokens):
        # Initialize the Parser object with a list of tokens
        self.tokens = tokens
        self.current_token = None
        self.next()  # Set the first token as current token

    def next(self):
        # Move to the next token from the input list
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def parse(self):
        # Start parsing the expression
        print('Parsing expression...')
        return self.expression()

    def expression(self):
        # Parse an expression involving terms
        print('Parsing expression: term')
        expr = self.term()  # Parse the term
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            if self.current_token.type == 'PLUS':
                # Parse addition operation
                print('Parsing expression: add')
                self.next()  # Move to the next token
                expr = ('ADD', expr, self.term())  # Create a node representing addition
            elif self.current_token.type == 'MINUS':
                # Parse subtraction operation
                print('Parsing expression: subtract')
                self.next()  # Move to the next token
                expr = ('SUB', expr, self.term())  # Create a node representing subtraction
        return expr

    def term(self):
        # Parse a term involving factors
        print('Parsing term: factor')
        term = self.factor()
        while self.current_token and self.current_token.type in ('TIMES', 'DIVIDE'):
            if self.current_token.type == 'TIMES':
                # Parse multiplication operation
                print('Parsing term: multiply')
                self.next()
                term = ('MUL', term, self.factor())  # Create a node representing multiplication
            elif self.current_token.type == 'DIVIDE':
                # Parse division operation
                print('Parsing term: divide')
                self.next()
                term = ('DIV', term, self.factor())  # Create a node representing division
        return term

    def factor(self):
        if self.current_token.type == 'NUMBER':
            # Parse a numeric value
            value = self.current_token.value
            print('Parsing factor: number {}'.format(value))
            self.next()
            return ('NUM', value)  # Create a node representing a numeric value
        elif self.current_token.type == 'LPAREN':
            # Parse an enclosed expression within parentheses
            print('Parsing factor: expression')
            self.next()
            value = self.expression()  # Parse the enclosed expression
            if self.current_token.type != 'RPAREN':
                raise Exception('Expected )')
            self.next()
            return value
        raise Exception('Unexpected token')
