class FiniteAutomaton:
    def __init__(self, automaton):
        self.states = automaton.states
        self.alphabet = automaton.alphabet
        self.transitions = automaton.transitions
        self.start = automaton.start
        self.final = automaton.accept_states

        def checkString(self, string):
            current = self.start
            for letter in string:
                if (current, letter) in self.transitions:
                    current = self.transitions[(current, letter)]
                else:
                    return False
            return current in self.final

        def checkStrings(self, strings):
            for string in strings:
                if self.checkString(string):
                    print(string, "accepted")
                else:
                    print(string, "rejected")
