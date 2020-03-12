"""
Testing rigor of an LZW implementation
"""

from pyhuffman import lzw


def test_lzw_encode_decode_ok():
    """Scenario: Symmetric encoding and decoding"""
    # Given a message to encode
    msg = "Super secret message"
    # When I encode the message
    encoded = lzw.encode(msg)
    # And decode the coded message
    decoded = lzw.decode(encoded)
    # Then the decoded message is the original
    assert decoded == msg, "Decoding an encoded message should return original"
