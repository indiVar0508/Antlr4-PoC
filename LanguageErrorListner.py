import sys
from antlr4 import *
from writeprogramParser import writeprogramParser
from writeprogramListener import writeprogramListener
from antlr4.error.ErrorListener import *
import io

class writeprogramErrorListener(ErrorListener):

    def __init__(self, output):
        self.output = output        
        self._symbol = ''
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text
        raise ErrorListener()

    @property        
    def symbol(self):
        return self._symbol