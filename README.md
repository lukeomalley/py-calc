# Python Calculator

Calculator written in python as a tool to learn about compilers.

This tool takes a mathematical equation as input:

```
500 + (10 * 20) - 200
```

It first scans the input and transforms it into tokens:

```python
tokens = [
  <TokenType.NUMBER '500'>,
  <TokenType.PLUS '+'>,
  <TokenType.LPAREN '(')>,
  <TokenType.NUMBER '10'>,
  <TokenType.STAR '*'>,
  <TokenType.NUMBER '20'>,
  <TokenType.RPAREN ')'>,
  <TokenType.MINUS '-'>,
  <TokenType.NUMBER '200'>,
]
```
