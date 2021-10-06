from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from Exo3Lexer import Exo3Lexer
from Exo3Parser import Exo3Parser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = Exo3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Exo3Parser(stream)
    parser.r()
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
