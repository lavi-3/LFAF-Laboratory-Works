import matplotlib.pyplot as plt
from Automaton import Automaton
from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars


class Main:

    def __init__(self):
        self.productions = {
            'S': ['aA', 'aB'],
            'A': ['bS'],
            'B': ['aC'],
            'C': ['a', 'bS'],
        }
        self.start_letter = 'S'
        self.grammar = grammar(self.productions, self.start_letter)
        self.finite_automaton = self.grammar.converttoFA()
        self.automaton = FiniteAutomaton

    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generateString()
            print(string)


if __name__ == '__main__':
    main = Main()

    main.generate_strings(5)

    automatons = main.grammar.converttoFA()

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

    checker = FiniteAutomaton(automaton)

    checker.checkStrings(['abababa', 'babac', 'ababaa', 'aa', 'aca', 'acacacab', 'cabca'])

    print(automatons)

automation = Automaton()

automation.states = ['q0', 'q1', 'q2', 'q3']
automation.alphabet = ['a', 'b']
automation.transitions = {
    ('q0', 'a'): ['q0'],
    ('q0', 'b'): ['q1'],
    ('q1', 'a'): ['q1', 'q2'],
    ('q1', 'b'): ['q3'],
    ('q2', 'a'): ['q2'],
    ('q2', 'b'): ['q3']}

automation.start_state = 'q0'
automation.accept_states = ['q3']
print('')
print('')
print('')
print('-----------------------------------------------------------------------------------------')
print('                                            LAB2')
print('-----------------------------------------------------------------------------------------')
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
