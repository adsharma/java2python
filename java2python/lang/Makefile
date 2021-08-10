.PHONY: all clean
.SILENT: clean

all: Java9Parser.py Java9Lexer.py


Java9Parser.py: Java9Parser.g4 Java9Lexer.py
	antlr4 -Dlanguage=Python3 Java9Lexer.g4


Java9Lexer.py: Java9Lexer.g4
	antlr4 -Dlanguage=Python3 Java9Parser.g4


clean:
	rm -f *.pyo
	rm -f *.pyc
	rm -f *Parser.py
	rm -f *Lexer.py
	rm -f *.tokens




