# Generated from writeprogram.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,2,1,2,1,2,3,2,25,8,2,3,2,
        27,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,
        2,1,0,8,11,1,0,2,7,33,0,12,1,0,0,0,2,19,1,0,0,0,4,26,1,0,0,0,6,28,
        1,0,0,0,8,32,1,0,0,0,10,34,1,0,0,0,12,13,3,2,1,0,13,15,5,1,0,0,14,
        16,3,4,2,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,1,1,0,0,0,19,20,7,0,0,0,20,3,1,0,0,0,21,27,3,6,3,0,22,25,3,
        8,4,0,23,25,5,16,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,27,1,0,0,0,26,
        21,1,0,0,0,26,24,1,0,0,0,27,5,1,0,0,0,28,29,5,14,0,0,29,30,3,10,
        5,0,30,31,5,14,0,0,31,7,1,0,0,0,32,33,5,15,0,0,33,9,1,0,0,0,34,35,
        7,1,0,0,35,11,1,0,0,0,3,17,24,26
    ]

class writeprogramParser ( Parser ):

    grammarFileName = "writeprogram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'+'", "'-'", "'/'", "'*'", "'%'", 
                     "'power'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "JAVA", "PYTHON", "CPP", "JS", "ARITHMETIC", "COMMUNICATE", 
                      "DIGITS", "TEXT", "WHITESPACE", "NEWLINE" ]

    RULE_command = 0
    RULE_language = 1
    RULE_statement = 2
    RULE_arithmentic = 3
    RULE_communication = 4
    RULE_operations = 5

    ruleNames =  [ "command", "language", "statement", "arithmentic", "communication", 
                   "operations" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    JAVA=8
    PYTHON=9
    CPP=10
    JS=11
    ARITHMETIC=12
    COMMUNICATE=13
    DIGITS=14
    TEXT=15
    WHITESPACE=16
    NEWLINE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def language(self):
            return self.getTypedRuleContext(writeprogramParser.LanguageContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(writeprogramParser.StatementContext)
            else:
                return self.getTypedRuleContext(writeprogramParser.StatementContext,i)


        def getRuleIndex(self):
            return writeprogramParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = writeprogramParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.language()
            self.state = 13
            self.match(writeprogramParser.T__0)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JAVA(self):
            return self.getToken(writeprogramParser.JAVA, 0)

        def PYTHON(self):
            return self.getToken(writeprogramParser.PYTHON, 0)

        def CPP(self):
            return self.getToken(writeprogramParser.CPP, 0)

        def JS(self):
            return self.getToken(writeprogramParser.JS, 0)

        def getRuleIndex(self):
            return writeprogramParser.RULE_language

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage" ):
                listener.enterLanguage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage" ):
                listener.exitLanguage(self)




    def language(self):

        localctx = writeprogramParser.LanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_language)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmentic(self):
            return self.getTypedRuleContext(writeprogramParser.ArithmenticContext,0)


        def communication(self):
            return self.getTypedRuleContext(writeprogramParser.CommunicationContext,0)


        def WHITESPACE(self):
            return self.getToken(writeprogramParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return writeprogramParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = writeprogramParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.arithmentic()
                pass
            elif token in [15, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 22
                    self.communication()
                    pass
                elif token in [16]:
                    self.state = 23
                    self.match(writeprogramParser.WHITESPACE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmenticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(writeprogramParser.DIGITS)
            else:
                return self.getToken(writeprogramParser.DIGITS, i)

        def operations(self):
            return self.getTypedRuleContext(writeprogramParser.OperationsContext,0)


        def getRuleIndex(self):
            return writeprogramParser.RULE_arithmentic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmentic" ):
                listener.enterArithmentic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmentic" ):
                listener.exitArithmentic(self)




    def arithmentic(self):

        localctx = writeprogramParser.ArithmenticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmentic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(writeprogramParser.DIGITS)
            self.state = 29
            self.operations()
            self.state = 30
            self.match(writeprogramParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommunicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(writeprogramParser.TEXT, 0)

        def getRuleIndex(self):
            return writeprogramParser.RULE_communication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommunication" ):
                listener.enterCommunication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommunication" ):
                listener.exitCommunication(self)




    def communication(self):

        localctx = writeprogramParser.CommunicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_communication)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(writeprogramParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return writeprogramParser.RULE_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperations" ):
                listener.enterOperations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperations" ):
                listener.exitOperations(self)




    def operations(self):

        localctx = writeprogramParser.OperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 252) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





