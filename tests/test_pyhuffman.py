import pytest
from pyhuffman import huffman

# Scenario: Showcase the strong typing
def test_simple_huffman():
    # Given a string symbol "1001" and probability 0.2
    symbol = huffman.Symbol("1001")
    probability = huffman.Probability(0.2)
    symbol_proba = tuple([symbol, probability])
    # When building a huffman table
    table = huffman.huffman_table(list(symbol_proba))
    # Then table makes sense
    assert table == 2, "Didn't even succeed at building a dumb table"
