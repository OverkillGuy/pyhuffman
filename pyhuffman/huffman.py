from typing import NewType, Tuple, Sequence


# A binary symbol to encode
Symbol = NewType("Symbol", str)

# The probability of an event
Probability = NewType("Probability", float)

# A pair of symbol and its probability of occurence
SymbolProbabilityPair = Tuple[Symbol, Probability]


def huffman_table(symbols_probas: Sequence[SymbolProbabilityPair]) -> int:
    return 2
