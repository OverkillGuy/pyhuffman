"""Huffman encoding implementation."""

from collections import Counter
from typing import Dict, Optional

# Pairs of symbol and their probability of occurence
SymbolTable = Dict[str, float]

# Original symbol and its huffman encoding
Encoding = Dict[str, str]


def huffman_table(symbols_probas: SymbolTable) -> Encoding:
    """Compute the huffman encoding table for given symbols/proba pairs.

    Args:
        symbols_probas: Dictionary mapping a symbol to its probability ∈ [0-1].

    Returns:
        Encoding dictionary mapping symbol to its encoded version
    """
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


def huffman_encode(
    message: str, table: Encoding, pad: Optional[bool] = None
) -> str:
    """Encode a message with huffman encoding.

    Args:
        message: The message payload to encode
        table: The encoding table to use for encoding. See `huffman_table`.
        pad: Optionally pad the output by zeroes to byte-align the output

    Returns:
        Encoded binary as a string
    """
    # just a lookup table, really
    encoded = "".join([table[c] for c in message])
    if pad:
        # Number of bits the incomplete byte will have
        encoded_leftover_byte = len(encoded) % 8
        n_padding = 8 - encoded_leftover_byte
        # We pad with ones, since the "symbol-delimiter" is 0
        encoded += "1" * n_padding
    return encoded


def huffman_decode(encoded: str, table: Encoding) -> str:
    """Decode a message encoded with huffman encoding.

    Args:
        encoded: The encoded message as binary string.
        table: The encoding table used for encoding/decoding.

    Returns:
        The decoded message as a string.
    """
    # will want encoded-to-decoded lookup table
    # = reverse the decoded-to-encoded table
    reversed_table = {v: k for k, v in table.items()}
    depadded = encoded.rstrip("1")
    acc = depadded  # copy the structure we'll be iterating over
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
    """Generate a huffman symbol table using a naive heuristic.

    Heuristic is to assume that characters are all equally likely to
    occur in given message

    Args:
        sample_message: A statistically representative sample of the kind of
            message we'll be encoding, used only to sample symbol (characters)
            list

    Returns:
        A symbol table using equi-probable symbols aka each symbol has 1/N
            proba, with N number of distinct characters used in the sample
            message.
    """
    unique_characters = set(sample_message)
    probability_of_character = 1.0 / len(unique_characters)
    return {c: probability_of_character for c in unique_characters}


def charcounter_table(sample_message: str) -> SymbolTable:
    """Generate a huffman symbol table using a char-frequency heuristic.

    Using character frequency to figure out how probable a character is.

    Args:
        sample_message: A statistically representative sample of the kind of
            message we'll be encoding, used to sample symbol (character)
            frequency.

    Returns:
        A symbol table using inverse-symbol-frequency.
    """
    # Counter returns a custom object mapping item to item-frequency
    # in a collection
    return dict(Counter(sample_message))
