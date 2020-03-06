from typing import Dict, Optional

# Pairs of symbol and their probability of occurence
SymbolTable = Dict[str, float]

# Original symbol and its huffman encoding
Encoding = Dict[str, str]


def huffman_table(symbols_probas: SymbolTable) -> Encoding:
    """ Computes the huffman encoding table for given symbols/proba pairs"""
    encoding_order = []
    symbols_acc = symbols_probas
    while symbols_probas:
        # Pick highest
        lowest_probability_symbol = max(symbols_acc, key=symbols_acc.get)
        del symbols_acc[lowest_probability_symbol]
        encoding_order.append(lowest_probability_symbol)
    encoding = {}
    for n, symbol in enumerate(encoding_order):
        encoding[symbol] = (n * "1") + "0"
    return encoding


def huffman_encode(message: str, table: Encoding) -> str:
    """ Encode a message with huffman encoding"""
    return "".join([table[c] for c in message])


def huffman_decode(encoded: str, table: Encoding) -> str:
    """ Decode a message encoded with huffman"""
    reversed_table = {v: k for k, v in table.items()}
    acc = encoded
    decoded = []
    while acc:  # Find symbol based on 0 delimiter
        current_index = 0
        while acc[current_index] != "0":
            current_index += 1
        # found a 0: read that symbol string and pop it off the buffer
        symbol = acc[: current_index + 1]
        decoded.append(reversed_table[symbol])
        acc = acc[current_index + 1 :]
    return "".join(decoded)


def equiprobable_table(sample_message: str) -> SymbolTable:
    """Generate a huffman symbol table using a superdumb heuristic

    Heuristic is to assume that characters are all equally likely to
    occur in given message
    """
    unique_characters = set(sample_message)
    probability_of_character = 1.0 / len(unique_characters)
    return {c: probability_of_character for c in unique_characters}


def charcounter_table(sample_message: str) -> SymbolTable:
    pass
