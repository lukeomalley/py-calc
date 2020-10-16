from enum import Enum


class TokenType(Enum):
    PLUS = 1
    MINUS = 2
    STAR = 3
    SLASH = 4


class Token:
    def __init__(self, type, lexeme, line, literal=None):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return f'<{self.type}, {self.lexeme}>'


class Scanner:
    def __init__(self, source):
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.source = source

    def scanTokens(self):
        while not self._isAtEnd():
            self.start = self.current
            self._scanToken()

        return self.tokens

    def _scanToken(self):
        c = self._nextToken()
        if c == '+':
            return self._addToken(TokenType.PLUS)
        elif c == '-':
            return self._addToken(TokenType.MINUS)
        elif c == '*':
            return self._addToken(TokenType.STAR)
        elif c == '/':
            return self._addToken(TokenType.SLASH)
        elif c == '\n':
            self.line += 1
        elif c == ' ' or '\t' or '\r':
            return

    def _isAtEnd(self):
        return self.current >= len(self.source)

    def _nextToken(self):
        self.current += 1
        return self.source[self.current - 1]

    def _addToken(self, tokenType, literal=None):
        lexeme = self.source[self.start:self.current]
        self.tokens.append(Token(tokenType, lexeme, self.line, literal))


if __name__ == "__main__":
    def main():
        program = input("> ")
        scanner = Scanner(program)
        tokens = scanner.scanTokens()
        print(tokens)

    main()
