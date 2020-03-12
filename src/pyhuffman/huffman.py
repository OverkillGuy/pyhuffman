"""
Huffman encoding implementation
"""

from collections import Counter
from typing import Dict

# Pairs of symbol and their probability of occurence
SymbolTable = Dict[str, float]

# Original symbol and its huffman encoding
Encoding = Dict[str, str]


def huffman_table(symbols_probas: SymbolTable) -> Encoding:
    """ Computes the huffman encoding table for given symbols/proba pairs"""
    encoding_order = []
    symbols_acc = symbols_probas
    while symbols_probas:  # Pick off highest probability until exhaustion
        lowest_probability_symbol = max(symbols_acc, key=symbols_acc.get)
        del symbols_acc[lowest_probability_symbol]
        encoding_order.append(lowest_probability_symbol)
    encoding = {}
    # Most likely symbol gets shortest encoding (0), and each
    # less-likely symbol after gets more and more 1s = longer to spell
    # out. 0 can be seen as "reserved for symbol-delimiter", see
    # decoding function
    for index, symbol in enumerate(encoding_order):
        encoding[symbol] = (index * "1") + "0"
    return encoding


def huffman_encode(message: str, table: Encoding) -> str:
    """ Encode a message with huffman encoding"""
    # just a lookup table, really
    return "".join([table[c] for c in message])


def huffman_decode(encoded: str, table: Encoding) -> str:
    """ Decode a message encoded with huffman"""
    # will want encoded-to-decoded lookup table
    # = reverse the decoded-to-encoded table
    reversed_table = {v: k for k, v in table.items()}
    acc = encoded  # copy the structure we'll be iterating over
    decoded = []
    while acc:
        # Find symbol based on 0 as delimiter:
        current_index = 0
        while acc[current_index] != "0":
            current_index += 1
        # found a 0 = a whole symbol
        symbol = acc[: current_index + 1]  # read that symbol
        decoded.append(reversed_table[symbol])  # decode it
        acc = acc[current_index + 1 :]  # and pop it off the accumulator
    return "".join(decoded)  # concatenate array-of-char to proper string


def equiprobable_table(sample_message: str) -> SymbolTable:
    """Generate a huffman symbol table using a naive heuristic

    Heuristic is to assume that characters are all equally likely to
    occur in given message
    """
    unique_characters = set(sample_message)
    probability_of_character = 1.0 / len(unique_characters)
    return {c: probability_of_character for c in unique_characters}


def charcounter_table(sample_message: str) -> SymbolTable:
    """Generate a huffman symbol table using a char-frequency heuristic

    Using character frequency to figure out how probable a character is
    """

    # Counter returns a custom object mapping item to item-frequency in a collection
    return dict(Counter(sample_message))


def encode_padded(msg: str, table: Encoding) -> str:
    """Counterpart of encode padding until byte alignment"""
    encoded = huffman_encode(msg, table)
    # Number of bits the incomplete byte will have
    encoded_leftover_byte = len(encoded) % 8
    n_padding = 8 - encoded_leftover_byte
    # We pad with ones, since the "symbol-delimiter" is 0
    return encoded + "1" * n_padding


def decode_padded(encoded: str, table: Encoding) -> str:
    """Counterpat of decode, stripping of padding first"""
    depadded = encoded.rstrip("1")
    return huffman_decode(depadded, table)
