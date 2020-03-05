import pytest
from pyhuffman.huffman import huffman_table, SymbolTable

# Scenario: Showcase the strong typing
def test_simple_huffman():
    # Given a string symbol "1001" and probability 0.2
    symbol_table = {"1001": 0.2}
    # When building a huffman table
    table = huffman_table(symbol_table)
    # Then table makes sense
    assert table == 2, "Didn't even succeed at building a dumb table"


# Scenario: Sample huffman table building
def test_example_huffman_table():
    """ From MIT course example"""
    # Given a symbol table of "{(A, 1/3)  (B, 1/2)  (C, 1/12)  (D, 1/12)}"
    symbols = {"A": 1 / 3.0, "B": 1 / 2.0, "C": 1 / 12.0, "D": 1 / 12.0}
