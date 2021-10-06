from antlr4 import InputStream
from antlr4 import CommonTokenStream

# include to use the generated lexer and parser
from Exo5Lexer import Exo5Lexer
from Exo5Parser import Exo5Parser

import sys


def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = Exo5Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Exo5Parser(stream)
    parser.r()
    print("Finished")


# warns pb if py file is included in others
if __name__ == '__main__':
    main()
