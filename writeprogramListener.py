# Generated from writeprogram.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .writeprogramParser import writeprogramParser
else:
    from writeprogramParser import writeprogramParser

# This class defines a complete listener for a parse tree produced by writeprogramParser.
class writeprogramListener(ParseTreeListener):

    # Enter a parse tree produced by writeprogramParser#command.
    def enterCommand(self, ctx:writeprogramParser.CommandContext):
        pass

    # Exit a parse tree produced by writeprogramParser#command.
    def exitCommand(self, ctx:writeprogramParser.CommandContext):
        pass


    # Enter a parse tree produced by writeprogramParser#language.
    def enterLanguage(self, ctx:writeprogramParser.LanguageContext):
        pass

    # Exit a parse tree produced by writeprogramParser#language.
    def exitLanguage(self, ctx:writeprogramParser.LanguageContext):
        pass


    # Enter a parse tree produced by writeprogramParser#statement.
    def enterStatement(self, ctx:writeprogramParser.StatementContext):
        pass

    # Exit a parse tree produced by writeprogramParser#statement.
    def exitStatement(self, ctx:writeprogramParser.StatementContext):
        pass


    # Enter a parse tree produced by writeprogramParser#arithmentic.
    def enterArithmentic(self, ctx:writeprogramParser.ArithmenticContext):
        pass

    # Exit a parse tree produced by writeprogramParser#arithmentic.
    def exitArithmentic(self, ctx:writeprogramParser.ArithmenticContext):
        pass


    # Enter a parse tree produced by writeprogramParser#communication.
    def enterCommunication(self, ctx:writeprogramParser.CommunicationContext):
        pass

    # Exit a parse tree produced by writeprogramParser#communication.
    def exitCommunication(self, ctx:writeprogramParser.CommunicationContext):
        pass


    # Enter a parse tree produced by writeprogramParser#operations.
    def enterOperations(self, ctx:writeprogramParser.OperationsContext):
        pass

    # Exit a parse tree produced by writeprogramParser#operations.
    def exitOperations(self, ctx:writeprogramParser.OperationsContext):
        pass



del writeprogramParser