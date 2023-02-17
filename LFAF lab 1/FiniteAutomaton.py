class FiniteAutomaton:
    # Initialize the given automaton's states, alphabet, transitions, start state, and final states.
    def __init__(self, automaton):
        self.states = automaton['states']
        self.alphabet = automaton['alphabet']
        self.transitions = automaton['transitions']
        self.start_state = automaton['start_state']
        self.final_states = automaton['final_states']

    def verify_string(self, string):
        current_state = self.start_state
        # Follow the corresponding transition if it exists for each symbol in the string.
        for symbol in string:
            try:
                current_state = self.transitions[current_state][symbol]
            except KeyError:
                # The string is invalid if the transition does not exist.
                return False

        return current_state in self.final_states

    def verify_strings(self, strings):
        print(f'------------------------------------------------------------------------')
        for string in strings:
            if self.verify_string(string):
                print(f'String "{string}" is accurate.')
                print(f'------------------------------------------------------------------------')
            else:
                print(f'String "{string}" is not accurate.')
                print(f'------------------------------------------------------------------------')
