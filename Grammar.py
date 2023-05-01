class Grammar:
    def __init__(self, productions, start_letter):
        self.productions = productions
        self.start_letter = start_letter

    def generateString(self):
        return self.generateStringFrom(self.start_letter)

    # noinspection PyUnreachableCode
    def converttoFA(self):
        start_state = 0
        automatons = {start_state: {}}
        state_count = 1

        for letter in self.productions:
            for productions in self.productions[letter]:
                current_state = start_state
                for s in productions:
                    if s not in productions:
                        if s not in automatons[current_state]:
                            automatons[current_state][s] = state_count
                            automatons[state_count] = {}
                            state_count += 1
                        current_state = automatons[current_state][s]
                        if current_state not in automatons:
                            automatons[current_state] = {}
                            automatons[current_state][' '] = start_state
                            return automatons

    def chomsky(self):
        for letter, productions in self.productions.items():
            for production in productions:
                if len(production) == 1 and production.islower():
                    continue
                elif len(production) == 2 and production.isupper():
                    continue
                elif len(production) == 1 and production.isupper():
                    return "Type 0, Unrestricted grammar"
                elif len(production) != 2 or not production.isupper():
                    return "Type 1, Context-sensitive grammar"

                if self.start_letter in 'ε' in self.productions[self.start_letter]:
                    if len(self.productions[self.start_letter]) > 1:
                        print("Type 2: Context-free grammar")
                    else:
                        print("Type 3: Context-free grammar")
