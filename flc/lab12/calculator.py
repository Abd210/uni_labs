from sly import Lexer, Parser
import math

class CalcLexer(Lexer):
    # Define the set of tokens including new ones for multiplication, division, power, factorial, and parentheses
    tokens = {
        NAME, NUMBER,
        PLUS, MINUS, TIMES, DIVIDE,
        POW, FACT,
        LPAREN, RPAREN,
        ASSIGN
    }

    # Ignored characters (space and tab)
    ignore = ' \t'

    # Token definitions using regular expressions
    NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'

    # Arithmetic operators
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    POW     = r'\^'
    FACT    = r'!'

    # Parentheses
    LPAREN  = r'\('
    RPAREN  = r'\)'

    # Assignment operator
    ASSIGN  = r'='

    # Ignored pattern for newlines to track line numbers
    ignore_newline = r'\n+'

    # Action to handle newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Error handling for illegal characters
    def error(self, t):
        print(f"Illegal character '{t.value[0]}' at line {self.lineno}")
        self.index += 1

class CalcParser(Parser):
    # Reference the tokens from the lexer
    tokens = CalcLexer.tokens

    # Define operator precedence and associativity
    precedence = (
        ('right', ASSIGN),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', POW),
        ('left', FACT),
        ('right', UMINUS),
    )

    def __init__(self):
        self.names = { }

    # Grammar rule for assignment statements
    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr
        print(f"{p.NAME} = {p.expr}")

    # Grammar rule for expressions (e.g., standalone expressions)
    @_('expr')
    def statement(self, p):
        print(p.expr)

    # Grammar rule for addition
    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    # Grammar rule for subtraction
    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    # Grammar rule for multiplication
    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    # Grammar rule for division with error handling for division by zero
    @_('expr DIVIDE expr')
    def expr(self, p):
        if p.expr1 == 0:
            print("Error: Division by zero")
            return 0
        return p.expr0 / p.expr1

    # Grammar rule for power (exponentiation)
    @_('expr POW expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    # Grammar rule for factorial (postfix operator)
    @_('expr FACT')
    def expr(self, p):
        if not isinstance(p.expr, int):
            print("Error: Factorial is only defined for integers")
            return 0
        if p.expr < 0:
            print("Error: Factorial is not defined for negative numbers")
            return 0
        try:
            return math.factorial(p.expr)
        except OverflowError:
            print("Error: Result too large")
            return 0

    # Grammar rule for unary minus
    @_('MINUS expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    # Grammar rule for expressions within parentheses
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    # Grammar rule for numbers
    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    # Grammar rule for variables
    @_('NAME')
    def expr(self, p):
        try:
            return self.names[p.NAME]
        except LookupError:
            print(f"Undefined name '{p.NAME}'")
            return 0

    # Error rule for syntax errors
    def error(self, p):
        if p:
            print(f"Syntax error at '{p.value}'")
            self.errok()
        else:
            print("Syntax error at EOF")

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    print("Welcome to the enhanced calculator!")
    print("Type 'exit' or press Ctrl+D to quit.")
    while True:
        try:
            text = input('calc > ')
            if text.lower() in ('exit', 'quit'):
                print("Goodbye!")
                break
        except EOFError:
            print("\nGoodbye!")
            break
        if text:
            parser.parse(lexer.tokenize(text))
