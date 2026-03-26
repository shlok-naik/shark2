input = """
x = 5
y = 10
z = x * y
z + (x+y)
"""

#tokens
NUMBER = 'NUMBER'
IDENTIFIER = 'IDENTIFIER'

PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MULTIPLY'
DIV = 'DIVIDE'

LBRAC = 'LBRACKET'
RBRAC = 'RBRACKET'

ASSIGN = 'ASSIGN'

EOF = 'EOF'

class token:
    def __init__(self, type_, value=None):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        if self.value is None:
            return f"({self.type_})"
        return f"({self.type_}, {self.value})"

#lexer
class lexer:
    def __init__(self, text):
        self.text = text
        self.currentPos = 0
        self.currentChar = text[0] if text else None

    def advance(self):
        self.currentPos += 1
        if self.currentPos >= len(self.text):
            self.currentChar = None
        else:
            self.currentChar = self.text[self.currentPos]

    def peek(self):
        peekPos = self.currentPos + 1
        if peekPos >= len(self.text):
            return None
        return self.text[peekPos]

    def do_number(self):
        num = ""
        num += self.currentChar
        while self.peek() is not None and (self.peek().isdigit() or self.peek() == "."):
            self.advance()
            num += self.currentChar
        return float(num)

    def do_identifier(self):
        ide = ""
        ide += self.currentChar
        while self.peek() is not None and (self.peek().isalpha() or self.currentChar == "_"):
            self.advance()
            ide += self.currentChar
        return ide

    def do_operator(self):
        if self.currentChar == "+":
            return PLUS
        elif self.currentChar == "-":
            return MINUS
        elif self.currentChar == "*":
            return MUL
        elif self.currentChar == "/":
            return DIV

    def do_brackets(self):
        if self.currentChar == "(":
            return LBRAC
        elif self.currentChar == ")":
            return RBRAC
                  
    def tokenise(self):
        tokens = []
        while self.currentChar != None:
            if self.currentChar.isdigit():
                tokens.append(token(NUMBER,self.do_number()))
                self.advance()
                
            elif self.currentChar.isalpha() or self.currentChar == "_":
                tokens.append(token(IDENTIFIER, self.do_identifier()))
                self.advance()
                
            elif self.currentChar in ["+", "-", "*", "/"]:
                tokens.append(token(self.do_operator()))
                self.advance()
                
            elif self.currentChar == "=":
                tokens.append(token(ASSIGN))
                self.advance()
                
            elif self.currentChar in ["(", ")"]:
                tokens.append(token(self.do_brackets()))
                self.advance()
                
            elif self.currentChar.isspace():
                self.advance()
                
            else:
                raise Exception(f"Unknown character: '{self.currentChar}'")
        return tokens
            
flexer = lexer(input)
print(flexer.tokenise())
                
                
                
            

    

