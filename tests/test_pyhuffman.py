"""
Simple tests for huffman encoding

Feature: Huffman coding
In order to send more messages per second
As a network engineer
I want to encode messages using Huffman coding
"""

from pyhuffman import huffman


def test_example_huffman_table():
    """Scenario: Sample huffman table building

    Sample message taken from MIT course example
    """
    # Given a symbol table of "{(A, 1/3)  (B, 1/2)  (C, 1/12)  (D, 1/12)}"
    symbols = {"A": 1 / 3.0, "B": 1 / 2.0, "C": 1 / 12.0, "D": 1 / 12.0}
    # When computing huffman table
    table = huffman.huffman_table(symbols)
    # Then the result is "{B: 0, A: 10, C: 110, D: 1110}"
    expected_table = {"B": "0", "A": "10", "C": "110", "D": "1110"}
    assert table == expected_table, "Incorrect table for sample problem"


def test_encode_decode_ok():
    """Scenario: Symmetric encoding and decoding"""
    # Given a message to encode
    msg = "Super secret message"
    # And a sample encoding table
    table = huffman.huffman_table(huffman.equiprobable_table(msg))
    # When I encode the message
    encoded = huffman.huffman_encode(msg, table)
    # And decode the coded message
    decoded = huffman.huffman_decode(encoded, table)
    # Then the decoded message is the original
    assert decoded == msg, "Decoding an encoded message should return original"


def test_better_heuristics_better_performance():
    """Scenario: Better heuristic gives better performance"""
    # Given a lorem ipsum text to encode
    msg = """Nullam eu ante vel est convallis dignissim. Donec vitae
    dolor. Lorem ipsum dolor sit amet, consectetuer adipiscing
    elit. Pellentesque dapibus suscipit ligula. Nullam tristique
    diam non turpis."""
    # When huffman encoding with naive table heuristic
    naive_table = huffman.huffman_table(huffman.equiprobable_table(msg))
    naive_encoding = huffman.huffman_encode(msg, naive_table)
    # And huffman encoding with character-frequency heuristic
    charfreq_table = huffman.huffman_table(huffman.charcounter_table(msg))
    charfreq_encoding = huffman.huffman_encode(msg, charfreq_table)
    # Then the character frequency heuristic's message is much shorter
    assert len(charfreq_encoding) < len(
        naive_encoding
    ), "Naive encoding shouldn't win here"


def test_byte_aligned_encoding():
    """ Scenario: Encoding and decoding with padding"""
    # Given a sample message
    msg = "Praesent fermentum tempor tellus.  Nunc porta vulputate tellus."
    # When I encode it for binary use
    table = huffman.huffman_table(huffman.charcounter_table(msg))
    padded_encoded = huffman.huffman_encode(msg, table, pad=True)
    # Then the encoded message is byte-aligned
    encoded_len = len(padded_encoded)
    assert encoded_len % 8 == 0, "Encoded message should be byte aligned"
    # When I decode it back
    decoded = huffman.huffman_decode(padded_encoded, table)
    # Then the message is still identical to original
    assert decoded == msg, "Decoded message should be identical to original"
