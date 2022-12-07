import io
import sys
from antlr4 import *
from writeprogramLexer import writeprogramLexer
from writeprogramParser import writeprogramParser
# from writeprogramListener import writeprogramListener as listner
from language_listner import LanguageListener as listner
# from LanguageErrorListner import writeprogramErrorListener

def main(argv):
    input = FileStream(argv[1]) # Get the Input, issue 
    lexer = writeprogramLexer(input)
    stream = CommonTokenStream(lexer)
    parser = writeprogramParser(stream)
    
    tree = parser.command()
    listner_obj = listner()
    walker = ParseTreeWalker()
    walker.walk(listner_obj, tree)
  

if __name__ == '__main__':
    main(sys.argv)