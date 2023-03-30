from lexer import Lexer
from os import name


def main():
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
