from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammar


class Main:

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
