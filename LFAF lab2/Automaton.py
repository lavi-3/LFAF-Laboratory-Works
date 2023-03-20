import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import self


class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'a', 'b'}
        self.start_state = 'q0'
        self.accept_states = {'q3'}
        self.transitions = {
            ('q0', 'a'): {'q0'},
            ('q0', 'b'): {'q1'},
            ('q1', 'a'): {'q1', 'q2'},
            ('q1', 'b'): {'q3'},
            ('q2', 'a'): {'q2'},
            ('q2', 'b'): {'q3'}
        }

        def deterministinize(self):
            for state in self.states:
                for letter in self.alphabet:
                    if (state, letter) not in self.transitions:
                     return False
            return True


def convertToDFA(self):
    if self.deterministinize():
        return self

    dfaStates = set()
    dfaAcceptStates = set()
    dfaTransitions = dict()
    stateQueue = [frozenset([self.start_state])]
    while stateQueue:
        currentStates = stateQueue.pop(0)
        dfaStates.add(currentStates)
        if any(state in self.accept_states for state in currentStates):
            dfaAcceptStates.add(currentStates)
        for letter in self.alphabet:
            nextStates = set()
            for state in currentStates:
                if (state, letter) in self.transitions:
                    nextStates.add(self.transitions[(state, letter)])
            nextStates = frozenset(nextStates)
            dfaTransitions[(currentStates, letter)] = nextStates
            if nextStates not in dfaStates:
                stateQueue.append(nextStates)

    dfa = Automaton()
    dfa.states = dfaStates
    dfa.accept_states = dfaAcceptStates
    dfa.transitions = dfaTransitions
    return dfa


def convertGrammar (self, letter):
    productions = dict()
    for state in self.states:
        next_states = self.transitions.get((state, letter), set())
        for next_state in next_states:
            if next_state in self.accept_states:
                if state not in productions:
                    productions[state] = set()
                productions[state].add(letter)
            else:
                if next_state not in productions:
                    productions[next_state] = set()
                productions[next_state].add(letter + next_state)

    start_letter = self.start_state
    if start_letter in productions:
        productions['S'] = productions[start_letter]
        del productions[start_letter]
        for state in self.states:
            for letter in self.alphabet:
                next_states = self.transitions.get((state, letter), set())
                for next_state in next_states:
                    if next_state in productions and letter + state in productions[state]:
                        if next_state not in productions:
                            productions[next_state] = set()
                            productions[next_state].add(letter + 'S')
    else:
        start_letter = 'S'
        productions[start_letter] = set()
        for accept_state in self.accept_states:
            productions[start_letter].add('eps' + accept_state)
            return start_letter, productions


def render(self):
    # Create a directed graph using networkx
    G = nx.DiGraph()

    # Add nodes to the graph
    for state in self.states:
        G.add_node(state, shape='circle')
    G.nodes[self.start_state]['shape'] = 'doublecircle'
    for state in self.accept_states:
        G.nodes[state]['peripheries'] = 2

    # Add edges to the graph
    for (from_state, letter), to_states in self.transitions.items():
        for to_state in to_states:
            G.add_edge(from_state, to_state, label=letter)

    # Set up positions for the nodes using networkx spring_layout
    pos = nx.spring_layout(G, seed=42)

    # Draw the graph using matplotlib
    nx.draw_networkx_nodes(G, pos, node_size=1000, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.8)
    nx.draw_networkx_labels(G, pos, font_size=18, font_family='sans-serif')
    edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=18, font_family='sans-serif')
    plt.axis('off')
    plt.show()
