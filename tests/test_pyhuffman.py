from pyhuffman import huffman

# Scenario: Sample huffman table building
def test_example_huffman_table():
    """ From MIT course example"""
    # Given a symbol table of "{(A, 1/3)  (B, 1/2)  (C, 1/12)  (D, 1/12)}"
    symbols = {"A": 1 / 3.0, "B": 1 / 2.0, "C": 1 / 12.0, "D": 1 / 12.0}
    # When computing huffman table
    table = huffman.huffman_table(symbols)
    # Then the result is "{B: 0, A: 10, C: 110, D: 1110}"
    expected_table = {"B": "0", "A": "10", "C": "110", "D": "1110"}
    assert table == expected_table, "Incorrect table for sample problem"


# Scenario: Symmetric encoding and decoding
def test_encode_decode_ok():
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
