from writeprogramParser import writeprogramParser
from writeprogramListener import writeprogramListener


class LanguageListener(writeprogramListener):

    def __init__(self):
        self.language = 'python3'
        self.code = ""
        self.file_format = {
            'python3': '.py', 'c++': '.cpp', 'java': '.java', 'javascript': '.js',  'js': '.js'
        }
        self.arithmetic_op = None
        self.statements = None
        self.intentation = '    '

    def output(self,statement):
        if self.language == 'python3':
            return f"print({statement})"
        elif self.language == 'c++':
            return f"cout<<{statement};"
        elif self.language == 'java':
            return f"System.out.println({statement});"
        elif self.language in ('js', 'javascript'):
            return f"console.log({statement});"

    def update_statement(self, content):
        if self.statements is None:
            self.statements = self.output(content)
        else:
            self.statements += '\n' + self.output(content)

    # Enter a parse tree produced by writeprogramParser#language.
    def enterLanguage(self, ctx:writeprogramParser.LanguageContext):
        self.language = ctx.getText().lower()
        if self.language == 'python3':
            self.code = "# BODY"
        elif self.language == 'c++':
            self.code = """
            #include<iostream>
            using namespace std;
            int main()
            {
                # BODY
                return 0;
            }
            """.strip().replace("            ", "")
        elif self.language == 'java':
            self.code = """public class myfirstclass{
                public static void main(String[] args){
                # BODY
                }
            }""".strip().replace("            ", "")
        else: # has to be javascript
            self.code = """# BODY""".strip()
    
    # Enter a parse tree produced by writeprogramParser#operations.
    def enterOperations(self, ctx:writeprogramParser.OperationsContext):
        op = ctx.getText()
        if op == 'power':
            if self.language == 'c++':
                self.arithmetic_op = "pow(#NUM1, #NUM2)"
            elif self.language == 'java' or self.language in ('js', 'javascript'):
                self.arithmetic_op = "Math.pow(#NUM1, #NUM2)"
            elif self.language == 'python3':
                self.arithmetic_op = "#NUM1 ** #NUM2"
        else:
            self.arithmetic_op = f"#NUM1 {op} #NUM2"
    
    # Exit a parse tree produced by writeprogramParser#operations.
    def exitOperations(self, ctx:writeprogramParser.OperationsContext):
        assert self.arithmetic_op is not None, "Couldn't figure out arithmetic operation."

    # Exit a parse tree produced by writeprogramParser#arithmentic.
    def exitArithmentic(self, ctx:writeprogramParser.ArithmenticContext):
        expr = ctx.getText()
        num1, num2 = expr.replace('power', ',').replace('*', ',').replace('+', ',').replace('-', ',').replace('/', ',').split(',')
        self.arithmetic_op = self.arithmetic_op.replace("#NUM1", num1).replace("#NUM2", num2)
        self.update_statement(self.arithmetic_op)
        self.arithmetic_op = ''

    # Exit a parse tree produced by writeprogramParser#command.
    def exitCommand(self, ctx:writeprogramParser.CommandContext):
        self.file = f"RequestedCode{self.file_format[self.language]}"
        self.code = self.code.replace("# BODY", self.statements)
        with open(self.file, "w") as f:
            f.write(self.code)

    # Exit a parse tree produced by writeprogramParser#statement.
    def exitStatement(self, ctx:writeprogramParser.StatementContext):
        # self.code = self.code.replace("# BODY", self.statements)
        self.arithmetic_op = ''

    # Enter a parse tree produced by writeprogramParser#communication.
    def enterCommunication(self, ctx:writeprogramParser.CommunicationContext):
        self.update_statement('"'+ctx.getText()+'"')
        