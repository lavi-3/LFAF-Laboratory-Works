# Chomsky Normal Form

**Course:** Formal Languages & Finite Automata  
**Author:** Cozlov Valeria \
**Variant:** 13

## Grammar


G=(VN, VI, P, S) Vn={S, A, B, C, D} VT={a, b}
P={ 
1. S → aB
2. S → DA
3. A → a
4. A → BD
5. A → bDAB
6. B → b
7. B → BA
8. D → ε
9. D → BA
10. C → BA}
## Theory

An algorithm for parsing and other language-processing tasks can be developed using the Chomsky Normal Form (CNF), a condensed version of context-free grammars. If all of a context-free grammar's production rules take one of the two following forms, it is considered to be in Chomsky Normal Form.
1. A -> BC, where A, B, and C are non-terminal symbols.
2. A -> a, where A is a non-terminal symbol, and a is a terminal symbol. 

Its simplicity, which makes it simpler to create algorithms that work with context-free grammars, is CNF's main advantage. Any context-free grammar can be transformed into its Chomsky Normal Form equivalent. The following steps are involved in the conversion process:
Eliminate -productions by substituting alternative productions that provide the same language without the -production for every production rule of the pattern A ->.
2. Get rid of renaming (unit productions): Substitute production rules for B in favor of production rules for A, where A and B are non-terminal symbols.
3. Remove symbols that are inaccessible: In the grammar, remove any non-terminal symbols that are inaccessible from the start symbol.
4. Remove useless symbols: Get rid of any symbols that aren't terminal and can't be used to create terminal strings.
5. Convert the remaining rules to CNF format: Divide any production rules that have more than two symbols into separate rules that follow the CNF structure.

By following these steps, we can transform any context-free grammar into an equivalent grammar in Chomsky Normal Form without altering the language it generates.

## Objectives

1. Implement a method for normalizing an input grammar by the rules of CNF (Chomsky Normal Form).
2. Encapsulate the implementation in a method with an appropriate signature (also ideally in an appropriate class/type).
3. Execute and test the implemented functionality.
4. (Bonus) Create unit tests that validate the functionality of the project.
5. (Bonus) Make the function accept any grammar, not only the one from the student's variant.

## Implementation description

### Eliminate Epsilon Productions

The task of eliminating -productions (i.e., rules in the form of A -> ) from the grammar is carried out via the 'eliminate_epsilon' method. To do this, all non-terminal symbols that produce either directly or indirectly are identified, and they are changed in all other production rules. With this replacement, the grammar's requirement for -productions is basically eliminated.

In order to normalize context-free grammars and bring them into compliance with the Chomsky Normal Form, -productions must be eliminated. By getting rid of ambiguity and making the grammar more predictable, this step aids in making parsing and other language processing activities more efficient.

### Eliminate Renaming
Unit productions (i.e., rules with the form A -> B, where A and B are non-terminal symbols) are removed from the provided grammar by the 'eliminate_renaming' method. To do this, all of the production rules connected to the referred non-terminal symbol are substituted for the unit production. Up until all unit productions have been eliminated from the grammar, the substitution process is carried out.

By using this technique, the grammatical structure can be made simpler and is guaranteed to follow Chomsky's Normal Form. Unit productions can be removed from grammar to simplify analysis and manipulation by lowering the number of rules and non-terminal symbols. Enhancing the effectiveness of parsing and other language processing activities is another benefit of this technique.

### Eliminate Inaccessible Symbols

Non-terminal symbols that cannot be reached from the grammar's start symbol are eliminated using the 'eliminateInaccessibleSymbols' component of the 'eliminate_renaming' function. All non-terminal symbols that can be reached from the initial symbol are iteratively found. Then, it eliminates any production rules with symbols that aren't reachable.

### Eliminate Non-Productive Symbols

Non-terminal symbols that are unable to generate any terminal strings are removed using the 'eliminate_nonproductive' method. All non-productive symbols are first identified, and any production rules containing them are then removed. By completing this stage, it is ensured that the grammar can produce at least one terminal string for each non-terminal symbol.

### Convert to Chomsky Normal Form
The remaining production rules are converted to the CNF format using the 'chomsky_normal_form' function. It accomplishes this by segmenting rules with more than two symbols on the right side into several rules that follow CNF. In rules with more than one symbol on the right side, it also introduces new non-terminal symbols to replace terminal symbols.

When these procedures are used in order, the input grammar is converted into an equivalent grammar in Chomsky Normal Form.

### Performing Unit Tests
This unit test class was created to examine how well the CNFConverter class performs the conversion of context-free grammars to Chomsky Normal Form. The test set consists of a variety of input grammars and tuples representing the predicted outcomes for each grammar. Each test in the suite checks to see if the output from the CNFConverter class's convert_to_cnf function corresponds to what was anticipated.The unit test class aids in validating the functionality of the CNFConverter class under various circumstances and inputs by testing various input grammars and anticipated outputs. Any failure in the unit tests gives a head start indication of any bugs or problems with the CNFConverter class, enabling quick fixes and enhancements.
# Results:
```
Original grammar:
({'C', 'B', "S'", 'D', 'S', 'A'}, {'b', 'a'}, [('S', ('a', 'B')), ('S', ('D', 'A')), ('A', ('a',)), ('A', ('B', 'D')), ('A', ('b', 'D', 'A', 'B')), ('B', ('b',)), ('B', ('B', 'A')), ('D', ()), ('D', ('B', 'A')), ('C', ('B', 'A'))], 'S')
Grammar in Chomsky normal form:
(set(), {'b', 'a'}, [('S', ('S',)), ('S', ('a',)), ('S', ('a',)), ('S', ('b',)), ('S', ('a',)), ('S', ('b',))], "S'")
All Tests Passed
Ran 4 tests in 0.001s
OK
```

# Conclusion
As a conclusion, I developed an algorithm to convert context-free grammars into Chomsky Normal Form, a particular form that makes grammar study and manipulation easier. The code uses data structures like lists, maps, and sets to manipulate productions, symbols, and productions. The implementation of sophisticated algorithms to change grammars, which can be helpful in natural language processing and other fields, made this lab work overall seem tough yet interesting.
