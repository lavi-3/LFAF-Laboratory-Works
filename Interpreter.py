class Interpreter:
    def __init__(self):
        # Initialize the Interpreter with an empty dictionary to store variables
        self.variables = {}

    def interpret(self, tree):
        # Interpret the given parse tree and return the result
        node_type = tree[0]

        if node_type == 'NUM':
            # If the node type is 'NUM', return the numeric value
            return float(tree[1])

        if node_type == 'ADD':
            # If the node type is 'ADD', interpret the left and right children recursively
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value + right_value

        if node_type == 'SUB':
            # If the node type is 'SUB', interpret the left and right children recursively
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value - right_value

        if node_type == 'MUL':
            # If the node type is 'MUL', interpret the left and right children recursively
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value * right_value

        if node_type == 'DIV':
            # If the node type is 'DIV', interpret the left and right children recursively
            left_value = self.interpret(tree[1])
            right_value = self.interpret(tree[2])
            return left_value / right_value

        # If an invalid node type is encountered, raise ValueError
        raise ValueError(f"Invalid node type: {node_type}")
