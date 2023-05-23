import unittest
from Automaton import Automaton
from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammar
from lexer import Lexer
from os import name
from CNFConverter import CNFConverter
from Tester import UnitTester


class Main:
    # LABORATORY WORK 1
    def __init__(self):
        # Create a context-free grammar by starting the class with a set of productions.
        self.productions = {
            'S': ['aB'],
            'B': ['aD', 'bB', 'cS'],
            'D': ['aD', 'bS', 'c'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammar(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.create_finite_automaton()
        self.automaton = FiniteAutomaton

    # Create a function that will generate strings from the grammar.
    def Create_string(self, n):
        for i in range(n):
            string = self.grammar.create_string()
            print(string)


if __name__ == '__main__':
    main = Main()
    main.Create_string(6)
    automatons = main.grammar.create_finite_automaton()
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        'alphabet': {'a', 'b', 'c'},
        'transitions': {
            'q0': {'a': 'q1'},
            'q1': {'a': 'q4', 'b': 'q2', 'c': 'q5'},
            'q2': {'a': 'q3', 'b': 'q2', 'c': 'q5'},
            'q3': {'a': 'q3', 'b': 'q4', 'c': 'q5'},
            'q4': {'a': 'q3', 'b': 'q2', 'c': 'q5'},
            'q5': {'a': 'q5', 'b': 'q0', 'c': 'q5'}
        },
        'start_state': 'q0',
        'final_states': {'q3', 'q5'}
    }
    verification = FiniteAutomaton(automaton)
    verification.verify_strings(['abababa', 'babac', 'ababaa', 'aa', 'aca', 'acacacab', 'cabca'])
    print('Automaton:', automatons)

# LABORATORY WORK 2
is_deterministic = automation.deterministinize()
print(f"Is automaton deterministic? {is_deterministic}")

# Convert NDFA to DFA
dfa = automation.convertToDFA()
print(f"DFA states: {dfa.states}")
print(f"DFA transition function: {dfa.transitions}")
print(f"DFA initial state: {dfa.start_state}")
print(f"DFA final states: {dfa.accept_states}")

# Convert automaton to regular grammar
grammar = automation.convertGrammar()
print(f"Regular grammar productions: {grammar}")
print(main.grammar.chomsky())
automation.render()


# LABORATORY WORK 3
sample_code = """
    var x = 42;
    var y = x + 5;
    print(y);
    """
lexer = Lexer(sample_code)
tokens = lexer.tokenize()

for token in tokens:
    print(token)

if name == "main":
    main()

    # LABORATORY WORK 4

non_terminal_symbols = {'S', 'A', 'B', 'C', 'D'}
terminal_symbols = {'a', 'b'}
productions = [
    ('S', ('a', 'B')),
    ('S', ('D', 'A')),
    ('A', ('a',)),
    ('A', ('B', 'D')),
    ('A', ('b', 'D', 'A', 'B')),
    ('B', ('b',)),
    ('B', ('B', 'A')),
    ('D', ()),
    ('D', ('B', 'A')),
    ('C', ('B', 'A'))
]
start_symbol = 'S'
grammar = (non_terminal_symbols, terminal_symbols, productions, start_symbol)

# Convert the grammar to Chomsky normal form
cnf_converter = CNFConverter(grammar)
cnf_grammar = cnf_converter.convert_to_cnf()

# Print the resulting grammar
print('Original grammar:')
print(grammar)
print('Grammar in Chomsky normal form:')
print(cnf_grammar)

print("All tests passed")

# Run unit tests
unittest.main()

# LABORATORY WORK 5


main_obj.process_expression("""
    var x = 42;
    var y = x + 5;
    print(y);""")

if __name__ == '__main__':
    main()
