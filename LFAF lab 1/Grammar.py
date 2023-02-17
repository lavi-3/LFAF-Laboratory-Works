import random
class Grammar:
    def __init__(self, productions, start_symbol):
        self.productions = productions
        self.start_symbol = start_symbol

    # Create a function that will generate a string from the grammar.
    def create_string(self):
        return self.generate_string(self.start_symbol)

    # DCreate a recursive function that will generate a string from the grammar.
    def generate_string(self, symbol):
        if symbol not in self.productions:
            return symbol
        production = random.choice(self.productions[symbol])
        return ''.join(self.generate_string(s) for s in production)

    def create_finite_automaton(self):
        start_state = 0
        automatons = {start_state: {}}
        count_state = 1

        for symbol in self.productions:
            for production in self.productions[symbol]:
                current_state = start_state
                for s in production:
                    if s not in automatons[current_state]:
                        # Add a new state and transition
                        automatons[current_state][s] = count_state
                        automatons[count_state] = {}
                        count_state += 1
                    current_state = automatons[current_state][s]
                # Add a transition to the last symbol's final state.
                if current_state not in automatons:
                    automatons[current_state] = {}
                automatons[current_state][''] = start_state

        return automatons
